salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
i=0
money_capital=0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(10):
    if i!=0:
        spend=spend*(1+increase)
    money_capital=money_capital+spend
    money_capital=money_capital-salary
money_capital=int(money_capital)+1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
