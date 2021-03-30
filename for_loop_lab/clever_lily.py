age = int(input())
price_of_washing_machine = float(input())
price_of_toy = int(input())

number_of_toys = 0
money_gathered = 0
money_for_birthday = 10
for i in range(1, age + 1):
    if i % 2 == 0:
        money_gathered += money_for_birthday
        money_for_birthday += 10
        money_gathered -= 1.00
    else:
        number_of_toys += 1

total_money = money_gathered + number_of_toys * price_of_toy

if total_money >= price_of_washing_machine:
    print(f'Yes!{total_money - price_of_washing_machine: .2f}')
else:
    print(f'No!{price_of_washing_machine - total_money: .2f}')
