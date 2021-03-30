budget = int(input())
season = input()
number_of_fishermen = int(input())

price = 0

if season == 'Spring':
    price = 3000
    if number_of_fishermen <= 6:
        price -= 0.1 * price
    elif 7 <= number_of_fishermen <= 11:
        price -= 0.15 * price
    elif number_of_fishermen >= 12:
        price -= 0.25 * price
elif season == 'Summer' or season == 'Autumn':
    price = 4200
    if number_of_fishermen <= 6:
        price -= 0.1 * price
    elif 7 <= number_of_fishermen <= 11:
        price -= 0.15 * price
    elif number_of_fishermen >= 12:
        price -= 0.25 * price
elif season == 'Winter':
    price = 2600
    if number_of_fishermen <= 6:
        price -= 0.1 * price
    elif 7 <= number_of_fishermen <= 11:
        price -= 0.15 * price
    elif number_of_fishermen >= 12:
        price -= 0.25 * price

if number_of_fishermen % 2 == 0 and not(season == 'Autumn'):
    price -= price * 0.05

if budget >= price:
    print(f'Yes! You have {budget - price:.2f} leva left.')
else:
    print(f'Not enough money! You need {price - budget:.2f} leva.')