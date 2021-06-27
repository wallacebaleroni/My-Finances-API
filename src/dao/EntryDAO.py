from src.dao.AccountDAO import *
from src.model.entry import *


class EntryDAO:
    def __init__(self):
        self._sqlite_conn = SqliteConnection()

    def get_all(self):
        command = "SELECT * FROM entry"
        results = self._sqlite_conn.execute_and_fetch(command)

        accountDAO = AccountDAO()

        entries = []
        for result in results:
            entry_id = result[0]
            account = accountDAO.get_by_id(result[1])
            date = result[2]
            seq = result[3]
            entry_type = result[4]
            value = result[5]
            if result[6] is not None:
                description = result[6]
            else:
                description = ""
            if result[7] is not None:
                commentary = result[7]
            else:
                commentary = ""

            entries.append(Entry(entry_id, account, date, seq, entry_type, value, description, commentary))

        return entries
