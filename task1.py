class SocialNetwork:
    """Базовый класс для социальных сетей"""
    
    def __init__(self, name: str, users_count: int, founded_year: int):
        self.name = name
        self._users_count = users_count  # инкапсулировано для контроля изменений
        self.founded_year = founded_year
    
    @property
    def users_count(self) -> int:
        return self._users_count
    
    def add_users(self, count: int) -> None:
        if count > 0:
            self._users_count += count
    
    def get_age(self) -> int:
        from datetime import datetime
        return datetime.now().year - self.founded_year
    
    def send_message(self, sender: str, receiver: str, text: str) -> bool:
        return True
    
    def __str__(self) -> str:
        return f'Социальная сеть "{self.name}" ({self.founded_year}), пользователей: {self._users_count}'
    
    def __repr__(self) -> str:
        return f"SocialNetwork(name={self.name!r}, users_count={self._users_count!r}, founded_year={self.founded_year!r})"


class VK(SocialNetwork):
    """Класс для социальной сети VK"""
    
    def __init__(self, name: str, users_count: int, founded_year: int, has_music: bool = True):
        super().__init__(name, users_count, founded_year)
        self.has_music = has_music
        self._vk_pay_enabled = True  # инкапсулировано для безопасности
    
    def listen_music(self, track_name: str) -> str:
        if self.has_music:
            return f"Воспроизводится: {track_name}"
        return "Музыкальный раздел недоступен"
    
    def send_message(self, sender: str, receiver: str, text: str) -> bool:
        """
        Перегружен для добавления специфичной для VK функциональности:
        поддержка стикеров VK, интеграция с VK Pay, возможность прикрепления музыки
        """
        if "[стикер]" in text.lower():
            return True
        if "[музыка]" in text.lower() and self.has_music:
            return True
        return super().send_message(sender, receiver, text)
    
    def __str__(self) -> str:
        music_status = "с музыкой" if self.has_music else "без музыки"
        return f'VK ({self.founded_year}), пользователей: {self._users_count}, {music_status}'
    
    def __repr__(self) -> str:
        return f"VK(name={self.name!r}, users_count={self._users_count!r}, founded_year={self.founded_year!r}, has_music={self.has_music!r})"


class Facebook(SocialNetwork):
    """Класс для социальной сети Facebook"""
    
    def __init__(self, name: str, users_count: int, founded_year: int, marketplace_enabled: bool = True):
        super().__init__(name, users_count, founded_year)
        self.marketplace_enabled = marketplace_enabled
        self._ad_revenue = 0.0  # инкапсулировано как коммерческая информация
    
    def create_marketplace_listing(self, item_name: str, price: float) -> str:
        if self.marketplace_enabled:
            return f"Объявление '{item_name}' создано за ${price}"
        return "Marketplace недоступен"
    
    def send_message(self, sender: str, receiver: str, text: str) -> bool:
        """
        Перегружен для добавления специфичной для Facebook функциональности:
        интеграция с Messenger, поддержка реакций, возможность отправки через WhatsApp
        """
        if "[реакция]" in text.lower():
            return True
        if "[whatsapp]" in text.lower():
            return True
        return super().send_message(sender, receiver, text)
    
    def __str__(self) -> str:
        marketplace_status = "с Marketplace" if self.marketplace_enabled else "без Marketplace"
        return f'Facebook ({self.founded_year}), пользователей: {self._users_count}, {marketplace_status}'
    
    def __repr__(self) -> str:
        return f"Facebook(name={self.name!r}, users_count={self._users_count!r}, founded_year={self.founded_year!r}, marketplace_enabled={self.marketplace_enabled!r})"



if __name__ == "__main__":
    print("=== Тестирование базового класса SocialNetwork ===")
    generic_network = SocialNetwork("MySocial", 1000000, 2020)
    print(str(generic_network))
    print(repr(generic_network))
    print(f"Возраст сети: {generic_network.get_age()} лет")
    generic_network.add_users(50000)
    print(f"После добавления пользователей: {generic_network.users_count}")
    
    print("\n=== Тестирование VK ===")
    vk = VK("VKontakte", 100000000, 2006, has_music=True)
    print(str(vk))
    print(repr(vk))
    print(f"Возраст VK: {vk.get_age()} лет")
    print(vk.listen_music("Группа Крови - Кино"))
    print(f"Отправка обычного сообщения: {vk.send_message('user1', 'user2', 'Привет!')}")
    print(f"Отправка стикера: {vk.send_message('user1', 'user2', 'Привет! [стикер]')}")
    
    print("\n=== Тестирование Facebook ===")
    fb = Facebook("Facebook", 2900000000, 2004, marketplace_enabled=True)
    print(str(fb))
    print(repr(fb))
    print(f"Возраст Facebook: {fb.get_age()} лет")
    print(fb.create_marketplace_listing("iPhone 13", 699.99))
    print(f"Отправка обычного сообщения: {fb.send_message('user1', 'user2', 'Hello!')}")
    print(f"Отправка с реакцией: {fb.send_message('user1', 'user2', 'Hello! [реакция]')}")
    
    print("\n=== Все классы работают корректно! ===")
