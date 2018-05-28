class CollectionObj:

    def __init__(self, id, title, author, publication_date, category, format, genre, full_price):
        self.id = id
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.category = category
        self.format = format
        self.genre = genre
        self.full_price = full_price

    def __str__(self):
        return "[{}]\t{}\n\t\tAuthor = {}\n\t\tPublication Date = {}\n\t\tCategory = {}\n\t\tFormat = {}\n\t\tGenre = {}\n\t\tFull Price = {}"\
            .format(self.id,
                    self.title,
                    self.author,
                    self.publication_date,
                    self.category,
                    self.format,
                    self.genre,
                    self.full_price)
