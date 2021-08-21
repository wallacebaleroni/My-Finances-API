class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

    def set_id(self, category_id):
        self.category_id = category_id

    def __dict__(self):
        category_dict = {'category_id': self.category_id, 'name': self.name}

        return category_dict
