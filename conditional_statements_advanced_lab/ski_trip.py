days = int(input())
room_type = input()
feedback = input()

nights = days - 1
percentage = 0
price = 0

if room_type == 'room for one person':
    price = 18.00
elif room_type == 'apartment':
    price = 25.00
elif room_type == 'president apartment':
    price = 35.00

if room_type == 'apartment':
    if nights < 10:
        percentage = 0.3
    elif 10 <= nights <= 15:
        percentage = 0.35
    elif nights > 15:
        percentage = 0.5
elif room_type == 'president apartment':
    if nights < 10:
        percentage = 0.1
    elif 10 <= nights <= 15:
        percentage = 0.15
    elif nights > 15:
        percentage = 0.2

discount = percentage * price
total_price = nights * price - nights * discount

if feedback == 'positive':
    total_price += total_price * 0.25
elif feedback == 'negative':
    total_price -= total_price * 0.10

print(f'{total_price:.2f}')