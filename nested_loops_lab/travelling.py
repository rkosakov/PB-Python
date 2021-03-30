destination = input()
while destination != 'End':
    budget = float(input())
    money_collected = 0
    while money_collected < budget:
        money = float(input())
        money_collected += money
    print(f'Going to {destination}!')
    destination = input()
