salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0

for i in range(0, months):
    if i != 0:
        spend = spend + spend*increase
    money_capital += spend - salary


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
