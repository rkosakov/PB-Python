budget = float(input())
season = input()

price_of_trip = 0
country = ''
place = ''

if season == 'winter':
    if budget <= 100:
        country = 'Bulgaria'
        place = 'Hotel'
        price_of_trip = budget * 0.70
    elif 101 <= budget <= 1000:
        country = 'Balkans'
        place = 'Hotel'
        price_of_trip = budget * 0.8
    elif budget > 1000:
        country = 'Europe'
        place = 'Hotel'
        price_of_trip = budget * 0.9

elif season == 'summer':
    if budget <= 100:
        country = 'Bulgaria'
        place = 'Camp'
        price_of_trip = budget * 0.30
    elif 101 <= budget <= 1000:
        country = 'Balkans'
        place = 'Camp'
        price_of_trip = budget * 0.40
    elif budget > 1000:
        country = 'Europe'
        place = 'Hotel'
        price_of_trip = budget * 0.90

print(f'Somewhere in {country}')
print(f'{place} - {price_of_trip:.2f}')

