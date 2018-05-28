class PatronObj:

    def __init__(self, patron_id, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.patron_id = patron_id

    def __str__(self):
        return "[{}] {} {}".format(self.patron_id, self.first_name, self.last_name)
