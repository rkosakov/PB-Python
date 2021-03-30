from math import floor
money = float(input())
coins_counter = 0
money_in_coins = floor(money * 100)
while money_in_coins != 0:
    if money_in_coins >= 200:
        money_in_coins -= 200
        coins_counter += 1
        continue
    elif money_in_coins >= 100:
        money_in_coins -= 100
        coins_counter += 1
        continue
    elif money_in_coins >= 50:
        money_in_coins -= 50
        coins_counter += 1
        continue
    elif money_in_coins >= 20:
        money_in_coins -= 20
        coins_counter += 1
        continue
    elif money_in_coins >= 10:
        money_in_coins -= 10
        coins_counter += 1
        continue
    elif money_in_coins >= 5:
        money_in_coins -= 5
        coins_counter += 1
        continue
    elif money_in_coins >= 2:
        money_in_coins -= 2
        coins_counter += 1
        continue
    elif money_in_coins >= 1:
        money_in_coins -= 1
        coins_counter += 1
        continue
print(coins_counter)