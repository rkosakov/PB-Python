budget = float(input())
people = int(input())
price_per_clothing = float(input())

decor_price = 0.1 * budget
if people > 150:
    price_per_clothing -= price_per_clothing * 0.10

price_clothing = price_per_clothing * people
total_expenses = price_clothing + decor_price
if budget >= total_expenses:
    print('Action!')
    print(f'Wingard starts filming with {budget - total_expenses:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {total_expenses - budget:.2f} leva more.')
