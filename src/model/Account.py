class Account:
    def __init__(self, account_id, name, account_type, color=0xFFFFFF):
        self.id = account_id
        self.name = name
        self.type = account_type
        self.color = color

    def set_id(self, account_id):
        self.id = account_id

    def __dict__(self):
        return {'id': self.id, 'name': self.name, 'type': self.type.name, 'color': self.color}
