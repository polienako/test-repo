class Smartphone:
    """Класс, описывающий смартфон"""
    
    def __init__(self, brand: str, battery_capacity: int, screen_size: float):
        """
        Инициализация смартфона
        
        :param brand: Бренд смартфона
        :param battery_capacity: Емкость батареи в mAh (должна быть положительной)
        :param screen_size: Размер экрана в дюймах (должен быть положительным)
        """
        if battery_capacity <= 0:
            raise ValueError("Емкость батареи должна быть положительной")
        if screen_size <= 0:
            raise ValueError("Размер экрана должен быть положительным")
        
        self.brand = brand
        self.battery_capacity = battery_capacity
        self.screen_size = screen_size
    
    def charge(self, minutes: int) -> int:
        """
        Зарядка смартфона
        
        :param minutes: Количество минут зарядки (должно быть положительным)
        :return: Процент заряда батареи после зарядки
        
        >>> phone = Smartphone("Apple", 3000, 6.1)
        >>> phone.charge(30)
        50
        """
        if minutes <= 0:
            raise ValueError("Время зарядки должно быть положительным")
        ...
    
    def install_app(self, app_name: str, app_size: float) -> bool:
        """
        Установка приложения на смартфон
        
        :param app_name: Название приложения
        :param app_size: Размер приложения в MB (должен быть положительным)
        :return: True если установка успешна, False иначе
        
        >>> phone = Smartphone("Samsung", 4000, 6.5)
        >>> phone.install_app("Instagram", 150.5)
        True
        """
        if app_size <= 0:
            raise ValueError("Размер приложения должен быть положительным")
        ...
    
    def make_call(self, phone_number: str, duration: int) -> str:
        """
        Совершение звонка
        
        :param phone_number: Номер телефона
        :param duration: Длительность звонка в секундах (должна быть положительной)
        :return: Статус звонка
        
        >>> phone = Smartphone("Xiaomi", 5000, 6.7)
        >>> phone.make_call("+79991234567", 120)
        'Звонок завершен'
        """
        if duration <= 0:
            raise ValueError("Длительность звонка должна быть положительной")
        ...


class CoffeeShop:
    """Класс, описывающий кофейню"""
    
    def __init__(self, name: str, capacity: int, rating: float):
        """
        Инициализация кофейни
        
        :param name: Название кофейни
        :param capacity: Вместимость посетителей (должна быть положительной)
        :param rating: Рейтинг кофейни от 0 до 5
        """
        if capacity <= 0:
            raise ValueError("Вместимость должна быть положительной")
        if not 0 <= rating <= 5:
            raise ValueError("Рейтинг должен быть от 0 до 5")
        
        self.name = name
        self.capacity = capacity
        self.rating = rating
    
    def serve_coffee(self, coffee_type: str, quantity: int) -> float:
        """
        Приготовление и подача кофе
        
        :param coffee_type: Тип кофе (эспрессо, капучино и т.д.)
        :param quantity: Количество порций (должно быть положительным)
        :return: Общая стоимость заказа
        
        >>> shop = CoffeeShop("Starbucks", 50, 4.5)
        >>> shop.serve_coffee("Капучино", 2)
        400.0
        """
        if quantity <= 0:
            raise ValueError("Количество порций должно быть положительным")
        ...
    
    def add_table(self, table_number: int, seats: int) -> bool:
        """
        Добавление столика в кофейню
        
        :param table_number: Номер столика (должен быть положительным)
        :param seats: Количество мест за столиком (должно быть положительным)
        :return: True если столик добавлен, False иначе
        
        >>> shop = CoffeeShop("Coffee House", 30, 4.2)
        >>> shop.add_table(5, 4)
        True
        """
        if table_number <= 0:
            raise ValueError("Номер столика должен быть положительным")
        if seats <= 0:
            raise ValueError("Количество мест должно быть положительным")
        ...


class VideoGame:
    """Класс, описывающий видеоигру"""
    
    def __init__(self, title: str, genre: str, price: float):
        """
        Инициализация видеоигры
        
        :param title: Название игры
        :param genre: Жанр игры
        :param price: Цена игры (должна быть неотрицательной)
        """
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        
        self.title = title
        self.genre = genre
        self.price = price
    
    def start_game(self, player_name: str) -> str:
        """
        Запуск игры
        
        :param player_name: Имя игрока
        :return: Приветственное сообщение
        
        >>> game = VideoGame("Cyberpunk 2077", "RPG", 1999.0)
        >>> game.start_game("Player1")
        'Добро пожаловать, Player1!'
        """
        ...
    
    def save_progress(self, save_slot: int, playtime: int) -> bool:
        """
        Сохранение прогресса игры
        
        :param save_slot: Номер слота сохранения (от 1 до 10)
        :param playtime: Время игры в минутах (должно быть неотрицательным)
        :return: True если сохранение успешно, False иначе
        
        >>> game = VideoGame("The Witcher 3", "RPG", 1499.0)
        >>> game.save_progress(1, 120)
        True
        """
        if not 1 <= save_slot <= 10:
            raise ValueError("Номер слота должен быть от 1 до 10")
        if playtime < 0:
            raise ValueError("Время игры не может быть отрицательным")
        ...
    
    def apply_discount(self, discount_percent: float) -> float:
        """
        Применение скидки к игре
        
        :param discount_percent: Процент скидки (от 0 до 100)
        :return: Новая цена после применения скидки
        
        >>> game = VideoGame("GTA V", "Action", 2000.0)
        >>> game.apply_discount(25)
        1500.0
        """
        if not 0 <= discount_percent <= 100:
            raise ValueError("Процент скидки должен быть от 0 до 100")
        ...



# Пример использования классов
if __name__ == "__main__":
    # Тестирование класса Smartphone
    print("=== Тестирование Smartphone ===")
    phone = Smartphone("Apple", 3000, 6.1)
    print(f"Создан смартфон: {phone.brand}, батарея {phone.battery_capacity} mAh, экран {phone.screen_size}\"")
    
    try:
        invalid_phone = Smartphone("Samsung", -1000, 6.5)
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
    
    # Тестирование класса CoffeeShop
    print("\n=== Тестирование CoffeeShop ===")
    shop = CoffeeShop("Starbucks", 50, 4.5)
    print(f"Создана кофейня: {shop.name}, вместимость {shop.capacity}, рейтинг {shop.rating}")
    
    try:
        invalid_shop = CoffeeShop("Coffee House", 30, 6.0)
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
    
    # Тестирование класса VideoGame
    print("\n=== Тестирование VideoGame ===")
    game = VideoGame("Cyberpunk 2077", "RPG", 1999.0)
    print(f"Создана игра: {game.title}, жанр {game.genre}, цена {game.price} руб.")
    
    try:
        invalid_game = VideoGame("GTA V", "Action", -500)
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
    
    print("\n=== Все классы работают корректно! ===")
