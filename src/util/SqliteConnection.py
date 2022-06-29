import sqlite3
import res.properties as properties


def open_sqlite_connection():
    database_name = "financeiro_test" if properties.is_test else "financeiro"

    connection = sqlite3.connect("res/" + database_name + ".db")
    cursor = connection.cursor()

    return connection, cursor


def close_sqlite_connection(connection, cursor):
    cursor.close()
    connection.close()


def execute(command):
    connection, cursor = open_sqlite_connection()

    try:
        cursor.execute(command)
        connection.commit()
        result = cursor.lastrowid
    except sqlite3.Error as er:
        print('Query: ' + command)
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        result = None
    finally:
        close_sqlite_connection(connection, cursor)

    return result


def execute_and_fetch(command):
    connection, cursor = open_sqlite_connection()

    try:
        cursor.execute(command)
        connection.commit()
        result = cursor.fetchall()
    except sqlite3.Error as er:
        print('Query: ' + command)
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        result = None
    finally:
        close_sqlite_connection(connection, cursor)

    return result


def create():
    connection, cursor = open_sqlite_connection()

    try:
        if properties.is_test:
            drop_tables(cursor)

        create_tables(cursor)

        if properties.is_test:
            populate(cursor)

        connection.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
    finally:
        close_sqlite_connection(connection, cursor)


def drop_tables(cursor):
    cursor.execute("""DROP TABLE IF EXISTS account""")
    cursor.execute("""DROP TABLE IF EXISTS entry""")


def create_tables(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS account(
                                    account_id  INTEGER     PRIMARY KEY     AUTOINCREMENT,
                                    name        TEXT        NOT NULL,
                                    type        TEXT        NOT NULL,
                                    color       TEXT,
                                    UNIQUE(name)
                                    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS entry(
                                    entry_id            INTEGER     PRIMARY KEY     AUTOINCREMENT,
                                    origin_account_id   INTEGER     NOT NULL,
                                    destiny_account_id  INTEGER,
                                    date                TEXT        NOT NULL,
                                    seq                 INTEGER     NOT NULL,
                                    category            TEXT        NOT NULL,
                                    value               INTEGER     NOT NULL,
                                    description         TEXT,
                                    commentary          TEXT,
                                    FOREIGN KEY(origin_account_id) REFERENCES account(account_id),
                                    FOREIGN KEY(destiny_account_id) REFERENCES account(account_id)
                                    )""")


def populate(cursor):
    cursor.execute("INSERT INTO account(name, type, color) VALUES ('Cartão', 'CREDIT_CARD', '#8e7cc3')")
    cursor.execute("INSERT INTO account(name, type, color) VALUES ('Santander', 'CHECKING_ACCOUNT', '#e06666')")
    cursor.execute("INSERT INTO account(name, type, color) VALUES ('NuConta', 'CHECKING_ACCOUNT', '#8e7cc3')")
    cursor.execute("""INSERT INTO entry(origin_account_id, date, seq, category, value, description, commentary)
                                  VALUES(1, '2021-07-09', 0, 'YIELD', 118, 'Rendimento NuConta', '');""")
    cursor.execute("""INSERT INTO entry(origin_account_id, date, seq, category, value, description, commentary)
                                  VALUES(2, '2021-07-09', 1, 'YIELD', 253, 'Rendimento PicPay', '');""")
    cursor.execute("""INSERT INTO entry(origin_account_id, date, seq, category, value, description, commentary)
                                  VALUES(1, '2021-07-09', 2, 'YIELD', 263, 'Rendimento NuConta', '');""")
