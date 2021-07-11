from src.dao.EntryDAO import *
from src.dao.AccountDAO import *


def get_all_accounts():
    accountDAO = AccountDAO()
    return accountDAO.get_all()


def get_account(account_id):
    accountDAO = AccountDAO()
    return accountDAO.get_by_id(account_id)


def create_account(name, account_type, color):
    accountDAO = AccountDAO()
    new_account = Account(-1, name, AccountType(account_type), color)
    result = accountDAO.save(new_account)
    if result is not None:
        new_account.set_id(result)
        return new_account
    return None


def get_all_entries():
    entryDAO = EntryDAO()
    return entryDAO.get_all()


def create_database():
    create()
