from src.util.SqliteConnection import *
from src.model.Entry import *
from src.dao.AccountDAO import AccountDAO


class EntryDAO:
    ENTRY_ID_REGISTER_INDEX = 0
    ACCOUNT_ID_REGISTER_INDEX = 1
    DATE_REGISTER_INDEX = 2
    SEQ_REGISTER_INDEX = 3
    CATEGORY_REGISTER_INDEX = 4
    VALUE_REGISTER_INDEX = 5
    DESCRIPTION_REGISTER_INDEX = 6
    COMMENTARY_REGISTER_INDEX = 7

    def get_all(self):
        command = "SELECT * FROM entry"
        results = execute_and_fetch(command)
        if results is None:
            return list

        return list(map(self.register_to_object, results))

    def get_by_account_id(self, account_id):
        command = "SELECT * FROM entry WHERE account_id={0}".format(account_id)
        results = execute_and_fetch(command)
        if results is None:
            return list()

        return list(map(self.register_to_object, results))

    def register_to_object(self, register):
        accountDAO = AccountDAO()

        entry_id = register[self.ENTRY_ID_REGISTER_INDEX]
        account = accountDAO.get_by_id(register[self.ACCOUNT_ID_REGISTER_INDEX])
        date = register[self.DATE_REGISTER_INDEX]
        seq = register[self.SEQ_REGISTER_INDEX]
        category = register[self.CATEGORY_REGISTER_INDEX]
        value = register[self.VALUE_REGISTER_INDEX]
        if register[self.DESCRIPTION_REGISTER_INDEX] is not None:
            description = register[self.DESCRIPTION_REGISTER_INDEX]
        else:
            description = ""
        if register[self.COMMENTARY_REGISTER_INDEX] is not None:
            commentary = register[self.COMMENTARY_REGISTER_INDEX]
        else:
            commentary = ""

        return Entry(entry_id, account, date, seq, category, value, description, commentary)
