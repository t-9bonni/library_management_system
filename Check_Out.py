class Check_OutObj:

    def __init__(self, id, patron_id, collection_id, date_checked_out, date_due, fine, total_fine, transaction_type):
        self.id = id
        self.patron_id = patron_id
        self.collection_id = collection_id
        self.date_checked_out = date_checked_out
        self.date_due = date_due
        self.fine = fine
        self.total_fine = total_fine
        self.transaction_type = transaction_type

    def __str__(self):
        return "ID = {}\n\t\tPatron ID = {}\n\t\tCollection ID = {}\n\t\tDate Checked Out = {}\n\t\tDate Due = {}\n\t\tFine = {}\n\t\tTotal Fine = {}\n\t\tTransaction Type = {}"\
            .format(self.id,
                    self.patron_id,
                    self.collection_id,
                    self.date_checked_out,
                    self.date_due,
                    self.fine,
                    self.total_fine,
                    self.transaction_type)
