month = input()
nights = int(input())

price_for_studio = 0
price_for_apartment = 0
if month == 'May' or month == 'October':
    price_for_studio = 50
    price_for_apartment = 65
    if nights > 14:
        price_for_studio -= price_for_studio * 0.30
        price_for_apartment -= price_for_apartment * 0.10
    elif nights > 7:
        price_for_studio -= price_for_studio * 0.05

if month == 'June' or month == 'September':
    price_for_studio = 75.20
    price_for_apartment = 68.70
    if nights > 14:
        price_for_studio -= price_for_studio * 0.20
        price_for_apartment -= price_for_apartment * 0.10
if month == 'July' or month == 'August':
    price_for_studio = 76
    price_for_apartment = 77
    if nights > 14:
        price_for_apartment -= price_for_apartment * 0.10

total_for_studio = price_for_studio * nights
total_for_apartment = price_for_apartment * nights

print(f'Apartment: {total_for_apartment:.2f} lv.')
print(f'Studio: {total_for_studio:.2f} lv.')
