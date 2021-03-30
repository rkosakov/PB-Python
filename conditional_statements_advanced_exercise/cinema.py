type_of_screening = input()
rows = int(input())
columns = int(input())

price = 0

if type_of_screening == 'Premiere':
    price = 12.00
elif type_of_screening == 'Normal':
    price = 7.50
elif type_of_screening == 'Discount':
    price = 5.00

total_income = rows * columns * price
print(f'{total_income:.2f}')
