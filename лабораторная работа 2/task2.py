salary = 5000
spend = 6000
months = 10
increase = 0.03

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
need = 0  #  подушка безопасности
current = spend  #  расходы

# проходим по всем месяцам
for month in range(1, months + 1):
    # зарплаты не хватает
    deficit = current - salary

    if deficit > 0:
        # добавляем дефицит к требуемой подушке
        need += deficit

    # увеличиваем расходы на следующий месяц
    current *= (1 + increase)

# округляем до целого числа
need = round(need)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", need)

