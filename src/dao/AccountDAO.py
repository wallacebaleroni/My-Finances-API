from src.dao.SqliteConnection import *
from src.model.Account import *


class AccountDAO:
    def __init__(self):
        self._sqlite_conn = SqliteConnection()

    def get_by_id(self, account_id):
        command = "SELECT * FROM account WHERE account_id={0}".format(account_id)

        result = self._sqlite_conn.execute_and_fetch(command)[0]

        name = result[1]
        account_type = result[2]
        color = result[3]
        if color is not None:
            return Account(account_id, name, account_type, color)
        else:
            return Account(account_id, name, account_type)
