class Entry:
    def __init__(self, entry_id, account, date, seq, category, value, description="", commentary=""):
        self.entry_id = entry_id
        self.account = account
        self.date = date
        self.seq = seq
        self.category = category
        self.value = value
        self.description = description
        self.commentary = commentary

    def __str__(self):
        value = self.get_formatted_value()
        return "|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|".format(self.entry_id, self.account.name, self.date, self.seq,
                                                          self.category, value, self.description, self.commentary)

    def get_value(self):
        return self.value / 100

    def get_formatted_value(self):
        return "{value:.2f}".format(value=self.get_value())
