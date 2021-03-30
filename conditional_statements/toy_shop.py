price_of_trip = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

total_sum = 2.60 * number_of_puzzles + 3 * number_of_dolls + 4.10 * number_of_bears + 8.20 * number_of_minions + 2 * number_of_trucks
toys_total = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks

if toys_total >= 50:
    total_sum -= total_sum * 0.25

total_sum -= total_sum * 0.10

if total_sum >= price_of_trip:
    print(f'Yes! {total_sum - price_of_trip :.2f} lv left.')
else:
    print(f'Not enough money! {price_of_trip - total_sum :.2f} lv needed.')