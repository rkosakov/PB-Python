money_needed = float(input())
money_available = float(input())

spend_counter = 0
days_counter = 0

while True:
    action = input()
    money = float(input())
    days_counter += 1

    if action == 'spend':
        spend_counter += 1
        money_available -= money
        if money_available < 0:
            money_available = 0
    elif action == 'save':
        spend_counter = 0
        money_available += money
    if spend_counter == 5:
        print("You can't save the money.")
        print(f'{days_counter}')
        exit(0)
    if money_available >= money_needed:
        break

print(f'You saved the money for {days_counter} days.')