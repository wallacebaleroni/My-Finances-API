from src.model.Category import *
from src.util.SqliteConnection import *


class CategoryDAO:
    CATEGORY_ID_REGISTER_INDEX = 0
    NAME_REGISTER_INDEX = 1

    def get_all(self):
        command = "SELECT * FROM category"
        results = execute_and_fetch(command)
        if results is None:
            return list

        return list(map(self.register_to_object, results))

    def register_to_object(self, register):
        category_id = register[self.CATEGORY_ID_REGISTER_INDEX]
        name = register[self.NAME_REGISTER_INDEX]

        return Category(category_id, name)
