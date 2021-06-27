from src.dao.SqliteConnection import *
from src.model.Account import *


class AccountDAO:
    ACCOUNT_ID_REGISTER_INDEX = 0
    NAME_REGISTER_INDEX = 1
    TYPE_REGISTER_INDEX = 2
    COLOR_REGISTER_INDEX = 3

    def __init__(self):
        self._sqlite_conn = SqliteConnection()

    def get_by_id(self, account_id):
        command = "SELECT * FROM account WHERE account_id={0}".format(account_id)

        result = self._sqlite_conn.execute_and_fetch(command)[0]

        return self.register_to_object(result)

    def get_all(self):
        command = "SELECT * FROM account"
        results = self._sqlite_conn.execute_and_fetch(command)
        if results is None:
            return []

        accounts = []
        for result in results:
            accounts.append(self.register_to_object(result))

        return accounts

    def register_to_object(self, register):
        account_id = register[self.ACCOUNT_ID_REGISTER_INDEX]
        name = register[self.NAME_REGISTER_INDEX]
        account_type = register[self.TYPE_REGISTER_INDEX]
        color = register[self.COLOR_REGISTER_INDEX]

        if color is not None:
            return Account(account_id, name, account_type, color)
        else:
            return Account(account_id, name, account_type)
