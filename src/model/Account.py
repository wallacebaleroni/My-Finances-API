class Account:
    def __init__(self, account_id, name, account_type, color):
        self.account_id = account_id
        self.name = name
        self.type = account_type
        self.color = color

    def set_id(self, account_id):
        self.account_id = account_id

    def __dict__(self):
        account_dict = {'account_id': self.account_id, 'name': self.name, 'type': self.type.name}

        if self.color is not None and self.color != "":
            account_dict['color'] = self.color

        return account_dict
