class Entry:
    def __init__(self, entry_id, origin_account, destiny_account, date, seq, category, value, description, commentary):
        self.entry_id = entry_id
        self.origin_account = origin_account
        self.destiny_account = destiny_account
        self.date = date
        self.seq = seq
        self.category = category
        self.value = value
        self.description = description
        self.commentary = commentary

    def __str__(self):
        value = self.get_formatted_value()
        return "|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|".format(self.entry_id, self.origin_account.name,
                                                              self.destiny_account.name, self.date, self.seq,
                                                              self.category, value, self.description, self.commentary)

    def __dict__(self):
        if self.destiny_account is None:
            destiny_account_id = None
        else:
            destiny_account_id = self.destiny_account.account_id

        return {'entry_id': self.entry_id, 'origin_account_id': self.origin_account.account_id,
                'destiny_account_id': destiny_account_id, 'date': self.date, 'seq': self.seq,
                'category': self.category, 'value': self.value, 'description': self.description,
                'commentary': self.commentary}

    def get_value(self):
        return self.value / 100

    def set_id(self, entry_id):
        self.entry_id = entry_id

    def set_seq(self, seq):
        self.seq = seq

    def get_formatted_value(self):
        return "{value:.2f}".format(value=self.get_value())
