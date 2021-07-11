from src.dao.SqliteConnection import *
from src.dao.EntryDAO import *
from src.dao.AccountDAO import *


class Controller:
    def __init__(self):
        self.entryDAO = EntryDAO()
        self.accountDAO = AccountDAO()

    def get_all_accounts(self):
        return self.accountDAO.get_all()

    def get_account(self, account_id):
        return self.accountDAO.get_by_id(account_id)

    def create_account(self, name, account_type, color):
        new_account = Account(-1, name, AccountType(account_type), color)
        result = self.accountDAO.save(new_account)
        if result is not None:
            new_account.set_id(result)
            return new_account
        return None

    def get_all_entries(self):
        return self.entryDAO.get_all()

    def create_database(self):
        create()
