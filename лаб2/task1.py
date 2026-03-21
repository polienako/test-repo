class Book:
    def __init__(self, id_, name, pages):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})"



if __name__ == "__main__":
    book = Book(id_=1, name='test_name_1', pages=200)
    print(str(book))
    print(repr(book))
