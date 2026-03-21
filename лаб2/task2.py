class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []

    def get_next_book_id(self):
        if not self.books:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


# Пример использования
if __name__ == "__main__":
    from book import Book
    
    # Создаем библиотеку с пустым списком
    lib = Library()
    print(f"Следующий ID для пустой библиотеки: {lib.get_next_book_id()}")
    
    # Добавляем книги
    book1 = Book(id_=1, name='Книга 1', pages=100)
    book2 = Book(id_=2, name='Книга 2', pages=200)
    lib.books.append(book1)
    lib.books.append(book2)
    
    print(f"Следующий ID после добавления книг: {lib.get_next_book_id()}")
    print(f"Индекс книги с id=1: {lib.get_index_by_book_id(1)}")
    print(f"Индекс книги с id=2: {lib.get_index_by_book_id(2)}")
    
    # Проверка ошибки
    try:
        lib.get_index_by_book_id(999)
    except ValueError as e:
        print(f"Ошибка: {e}")
