salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

required_capital = 0
current_spend = spend
month = 0
for month in range(months):
    deficit = current_spend - salary
    if deficit > 0:
        required_capital += deficit
    current_spend *= (1 + increase)
    month += 1
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(required_capital))
