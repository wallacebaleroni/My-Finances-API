from src.util.SqliteConnection import *
from src.model.Account import *
from src.model.AccountType import *


class AccountDAO:
    ACCOUNT_ID_REGISTER_INDEX = 0
    NAME_REGISTER_INDEX = 1
    TYPE_REGISTER_INDEX = 2
    COLOR_REGISTER_INDEX = 3

    def get_by_id(self, account_id):
        command = "SELECT * FROM account WHERE account_id={0}".format(account_id)

        result = execute_and_fetch(command)
        if len(result) > 0:
            result = self.register_to_object(result[0])
        else:
            print("Account with id='{0}' not found on database".format(account_id))
            result = None

        return result

    def get_all(self):
        command = "SELECT * FROM account"
        results = execute_and_fetch(command)
        if results is None:
            return list

        return list(map(self.register_to_object, results))

    def save(self, account):
        command = "INSERT INTO account(name, type, color) VALUES('{0}', '{1}', '{2}')"\
            .format(account.name, account.type.value, account.color)
        result = execute(command)
        return result

    def register_to_object(self, register):
        account_id = register[self.ACCOUNT_ID_REGISTER_INDEX]
        name = register[self.NAME_REGISTER_INDEX]
        account_type = AccountType(register[self.TYPE_REGISTER_INDEX])
        color = register[self.COLOR_REGISTER_INDEX]

        if color is not None:
            return Account(account_id, name, account_type, color)
        else:
            return Account(account_id, name, account_type, "")
