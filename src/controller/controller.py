from src.dao.EntryDAO import *
from src.dao.AccountDAO import *


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


def get_all_entries():
    entryDAO = EntryDAO()
    return entryDAO.get_all()


def get_entry(entry_id):
    entryDAO = EntryDAO()
    return entryDAO.get_by_id(entry_id)


def create_entry(account_id, date, category, value, description, commentary):
    entryDAO = EntryDAO()
    accountDAO = AccountDAO()

    account = accountDAO.get_by_id(account_id)
    if account is None:
        return None

    new_entry = Entry(-1, account, date, -1, category, value, description, commentary)
    entry_id, seq = entryDAO.save(new_entry)
    if entry_id is not None:
        new_entry.set_id(entry_id)
        new_entry.set_seq(seq)
        return new_entry
    return None


def create_database():
    create()
