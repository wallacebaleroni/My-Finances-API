from src.util.SqliteConnection import *
from src.model.Entry import *
from src.dao.AccountDAO import AccountDAO


class EntryDAO:
    ENTRY_ID_REGISTER_INDEX = 0
    ORIGIN_ACCOUNT_ID_REGISTER_INDEX = 1
    DESTINY_ACCOUNT_ID_REGISTER_INDEX = 2
    DATE_REGISTER_INDEX = 3
    SEQ_REGISTER_INDEX = 4
    CATEGORY_REGISTER_INDEX = 5
    VALUE_REGISTER_INDEX = 6
    DESCRIPTION_REGISTER_INDEX = 7
    COMMENTARY_REGISTER_INDEX = 8

    def get_by_id(self, entry_id):
        command = "SELECT * FROM entry WHERE entry_id={0}".format(entry_id)

        result = execute_and_fetch(command)
        if len(result) > 0:
            result = self.register_to_object(result[0])
        else:
            print("Entry with id='{0}' not found on database".format(entry_id))
            result = None

        return result

    def get_all(self):
        command = "SELECT * FROM entry"
        results = execute_and_fetch(command)
        if results is None:
            return list()

        return list(map(self.register_to_object, results))

    def get_with_params(self, params):
        conditions = []
        if 'category' in params.keys():
            conditions.append("category='{0}'".format(params['category']))
        if 'initial_date' in params.keys():
            conditions.append("date>'{0}'".format(params['initial_date']))
        if 'final_date' in params.keys():
            conditions.append("date<'{0}'".format(params['final_date']))
        if 'origin_account' in params.keys():
            conditions.append("origin_account_id='{0}'".format(params['origin_account']))
        if 'destiny_account' in params.keys():
            conditions.append("destiny_account_id='{0}'".format(params['destiny_account']))

        if len(conditions) == 0:
            return self.get_all()

        command = "SELECT * FROM entry WHERE"
        for i in range(len(conditions)):
            if i == 0:
                command += " " + conditions[i]
            else:
                command += " AND " + conditions[i]

        results = execute_and_fetch(command)
        if results is None:
            return list()

        return list(map(self.register_to_object, results))

    def get_by_account_id(self, account_id):
        command = "SELECT * FROM entry WHERE origin_account_id={0} OR destiny_account_id={0}".format(account_id)
        results = execute_and_fetch(command)
        if results is None:
            return list()

        return list(map(self.register_to_object, results))

    def get_last_seq(self, date):
        command = "SELECT MAX(seq) FROM entry WHERE date='{0}'".format(date)
        results = execute_and_fetch(command)[0][0]
        if results is None:
            return 0
        return results

    def save(self, entry):
        new_seq = self.get_last_seq(entry.date) + 1

        if entry.destiny_account is not None:
            destiny_account_id = entry.destiny_account.account_id
        else:
            destiny_account_id = "NULL"

        command = "INSERT INTO " \
                  "entry(origin_account_id, destiny_account_id, date, seq, category, value, description, commentary) " \
                  "VALUES({0}, {1}, '{2}', {3}, '{4}', {5}, '{6}', '{7}');" \
            .format(entry.origin_account.account_id, destiny_account_id, entry.date, new_seq,
                    entry.category, entry.value, entry.description, entry.commentary)
        result = execute(command)
        return result, new_seq

    def register_to_object(self, register):
        accountDAO = AccountDAO()

        entry_id = register[self.ENTRY_ID_REGISTER_INDEX]
        origin_account = accountDAO.get_by_id(register[self.ORIGIN_ACCOUNT_ID_REGISTER_INDEX])
        if register[self.DESTINY_ACCOUNT_ID_REGISTER_INDEX] is not None:
            destiny_account = accountDAO.get_by_id(register[self.DESTINY_ACCOUNT_ID_REGISTER_INDEX])
        else:
            destiny_account = None
        date = register[self.DATE_REGISTER_INDEX]
        seq = register[self.SEQ_REGISTER_INDEX]
        category = register[self.CATEGORY_REGISTER_INDEX]
        value = register[self.VALUE_REGISTER_INDEX]
        description = register[self.DESCRIPTION_REGISTER_INDEX]
        commentary = register[self.COMMENTARY_REGISTER_INDEX]

        return Entry(entry_id, origin_account, destiny_account, date, seq, category, value, description, commentary)
