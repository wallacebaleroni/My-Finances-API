import sqlite3


def open_sqlite_connection():
    connection = sqlite3.connect("res/financeiro.db")
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
        cursor.execute("""CREATE TABLE IF NOT EXISTS account(
                                account_id  INTEGER     PRIMARY KEY     AUTOINCREMENT,
                                name        TEXT        NOT NULL,
                                type        TEXT        NOT NULL,
                                color       TEXT
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
        connection.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
    finally:
        close_sqlite_connection(connection, cursor)
