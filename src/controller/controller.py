from src.dao.EntryDAO import *


class Controller:
    def __init__(self):
        self.entryDAO = EntryDAO()

    def get_all_entries(self):
        return self.entryDAO.get_all()
