import sqlite3


class SqliteConnection:
    def __init__(self):
        self._connection = sqlite3.connect("res/financeiro.db")
        self._cursor = self._connection.cursor()
        self.create()

    def create(self):
        self._cursor.execute("""CREATE TABLE IF NOT EXISTS account(
                                account_id  INTEGER     PRIMARY KEY     AUTOINCREMENT,
                                name        TEXT        NOT NULL,
                                type        TEXT        NOT NULL,
                                color       TEXT
                                )""")
        self._cursor.execute("""CREATE TABLE IF NOT EXISTS entry(
                                entry_id    INTEGER     PRIMARY KEY     AUTOINCREMENT,
                                account_id  INTEGER     NOT NULL,
                                date        TEXT        NOT NULL,
                                seq         INTEGER     NOT NULL,
                                category    TEXT        NOT NULL,
                                value       INTEGER     NOT NULL,
                                description TEXT,
                                commentary  TEXT,
                                FOREIGN KEY(account_id) REFERENCES account(account_id)
                                )""")
        self._connection.commit()

    def close(self):
        self._cursor.close()
        self._connection.close()

    def execute(self, command):
        # Maybe this should have a try/catch
        self._cursor.execute(command)
        self._connection.commit()
        return True

    def execute_and_fetch(self, command):
        # Maybe this should have a try/catch
        self._cursor.execute(command)
        self._connection.commit()
        return self._cursor.fetchall()
