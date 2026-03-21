class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def author(self) -> str:
        return self._author
    
    def __str__(self) -> str:
        return f'Книга "{self.name}". Автор: {self.author}'
    
    def __repr__(self) -> str:
        return f"Book(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages
    
    @property
    def pages(self) -> int:
        return self._pages
    
    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value
    
    def __str__(self) -> str:
        return f'Книга "{self.name}". Автор: {self.author}. Страниц: {self.pages}'
    
    def __repr__(self) -> str:
        return f"PaperBook(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
    
    @property
    def duration(self) -> float:
        return self._duration
    
    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной")
        self._duration = float(value)
    
    def __str__(self) -> str:
        return f'Книга "{self.name}". Автор: {self.author}. Продолжительность: {self.duration} ч'
    
    def __repr__(self) -> str:
        return f"AudioBook(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"



# Пример использования
if __name__ == "__main__":
    print("=== Тестирование базового класса Book ===")
    book = Book("Война и мир", "Лев Толстой")
    print(str(book))
    print(repr(book))
    
    print("\n=== Тестирование PaperBook ===")
    paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
    print(str(paper_book))
    print(repr(paper_book))
    
    # Проверка неизменяемости name и author
    try:
        paper_book.name = "Новое название"
    except AttributeError as e:
        print(f"Ошибка: невозможно изменить название - {e}")
    
    # Проверка валидации pages
    try:
        paper_book.pages = -100
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
    
    try:
        paper_book.pages = "триста"
    except TypeError as e:
        print(f"Ошибка типа: {e}")
    
    print("\n=== Тестирование AudioBook ===")
    audio_book = AudioBook("Гарри Поттер", "Дж. К. Роулинг", 8.5)
    print(str(audio_book))
    print(repr(audio_book))
    
    # Проверка валидации duration
    try:
        audio_book.duration = -5.0
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
    
    try:
        audio_book.duration = "десять"
    except TypeError as e:
        print(f"Ошибка типа: {e}")
    
    print("\n=== Все классы работают корректно! ===")
