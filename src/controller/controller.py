from src.dao.EntryDAO import *
from src.dao.AccountDAO import *


class Controller:
    def __init__(self):
        self.entryDAO = EntryDAO()
        self.accountDAO = AccountDAO()

    def get_all_entries(self):
        return self.entryDAO.get_all()

    def get_all_accounts(self):
        return self.accountDAO.get_all()
