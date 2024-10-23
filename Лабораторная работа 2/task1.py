money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
dolg=0
month=0
first_month=0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while dolg==0:
    if first_month==0:
        dolg=spend-salary
        money_capital=money_capital-dolg
        month=month+1
        first_month=first_month+1
        dolg=0
    else:
        spend = spend * (1 + increase)
        dolg = spend - salary
        if dolg<=money_capital:
            money_capital = money_capital - dolg
            month = month + 1
            dolg = 0
        else:
            break

print("Количество месяцев, которое можно протянуть без долгов:", month)
