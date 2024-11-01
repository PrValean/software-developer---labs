money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0

while True:
    difference = spend - salary

    if difference > money_capital:
        break

    spend = spend + spend*increase
    money_capital -= difference
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
