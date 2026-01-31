money_capital = 20000  # Подушка безопасности
salary = 5000  # Зарплата
spend = 6000  # Траты
increase = 0.05  # Рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0
while True:
    available_money = money_capital + salary
    if available_money >= spend:
        money_capital = available_money - spend
        months += 1
        spend *= (1 + increase)
    else:
        break


print("Количество месяцев, которое можно протянуть без долгов:", months)

