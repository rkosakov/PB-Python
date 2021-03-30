days = int(input())
number_of_bakers = int(input())
number_of_cakes = int(input())
number_of_waffles = int(input())
number_of_pancakes = int(input())

cakes = 45 * number_of_cakes
waffles = 5.80 * number_of_waffles
pancakes = 3.20 * number_of_pancakes

total_per_day = (cakes + waffles + pancakes) * number_of_bakers
total = total_per_day * days

total_after_expenses = total - (1/8 * total)
print(total_after_expenses)