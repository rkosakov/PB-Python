flower = input()
number_of_flowers = int(input())
budget = int(input())

price = 0
if flower == 'Roses':
    price = 5
    if number_of_flowers > 80:
        price -= 0.10 * 5
elif flower == 'Dahlias':
    price = 3.80
    if number_of_flowers > 90:
        price -= 0.15 * 3.80
elif flower == 'Tulips':
    price = 2.80
    if number_of_flowers > 80:
        price -= 0.15 * 2.8
elif flower == 'Narcissus':
    price = 3
    if number_of_flowers < 120:
        price += 3 * 0.15
elif flower == 'Gladiolus':
    price = 2.5
    if number_of_flowers < 80:
        price += 2.5 * 0.20

total_price = number_of_flowers * price

if budget >= total_price:
    print(f'Hey, you have a great garden with {number_of_flowers} {flower} and {budget - total_price:.2f} leva left.')
else:
    print(f'Not enough money, you need {total_price - budget:.2f} leva more.')