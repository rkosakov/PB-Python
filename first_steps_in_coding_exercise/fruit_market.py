price_of_strawberries = float(input())
kilograms_of_bananas = float(input())
kilograms_of_oranges = float(input())
kilograms_of_raspberries = float(input())
kilograms_of_strawberries = float(input())

price_of_raspberries = price_of_strawberries / 2
price_of_oranges = price_of_raspberries - (0.40 * price_of_raspberries)
price_of_bananas = price_of_raspberries - (0.8 * price_of_raspberries)

raspberries = kilograms_of_raspberries * price_of_raspberries
oranges = price_of_oranges * kilograms_of_oranges
bananas = price_of_bananas * kilograms_of_bananas
strawberries = price_of_strawberries * kilograms_of_strawberries

total = raspberries + oranges + bananas + strawberries
print(total)
