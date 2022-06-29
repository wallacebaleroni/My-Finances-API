from src.dao.EntryDAO import *
from src.dao.AccountDAO import *
from src.dao.CategoryDAO import *


def get_all_accounts():
    accountDAO = AccountDAO()
    return accountDAO.get_all()


def get_account(account_id):
    accountDAO = AccountDAO()
    return accountDAO.get_by_id(account_id)


def get_entries_by_account(account_id):
    if get_account(account_id) is None:
        return None

    entryDAO = EntryDAO()
    return entryDAO.get_by_account_id(account_id)


def create_account(name, account_type, color):
    accountDAO = AccountDAO()
    new_account = Account(-1, name, AccountType(account_type), color)
    account_id = accountDAO.save(new_account)
    if account_id is not None:
        new_account.set_id(account_id)
        return new_account
    return None


def get_all_entries(params):
    entryDAO = EntryDAO()

    if len(params) != 0:
        return entryDAO.get_with_params(params)

    return entryDAO.get_all()


def get_entry(entry_id):
    entryDAO = EntryDAO()
    return entryDAO.get_by_id(entry_id)


def create_entry(origin_account_id, destiny_account_id, date, category, value, description, commentary):
    entryDAO = EntryDAO()
    accountDAO = AccountDAO()

    origin_account = accountDAO.get_by_id(origin_account_id)
    if origin_account is None:
        return None

    if destiny_account_id is not None:
        destiny_account = accountDAO.get_by_id(destiny_account_id)
    else:
        destiny_account = None

    new_entry = Entry(-1, origin_account, destiny_account, date, -1, category, value, description, commentary)
    entry_id, seq = entryDAO.save(new_entry)
    if entry_id is not None:
        new_entry.set_id(entry_id)
        new_entry.set_seq(seq)
        return new_entry
    return None


def get_all_categories():
    categoryDAO = CategoryDAO()
    return categoryDAO.get_all()


def create_database():
    create()
