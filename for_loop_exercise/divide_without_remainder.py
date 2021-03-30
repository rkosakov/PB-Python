numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
n1 = 0
n2 = 0
n3 = 0

for i in range(numbers):
    number = int(input())
    if number % 2 == 0:
        n1 += 1
    if number % 3 == 0:
        n2 += 1
    if number % 4 == 0:
        n3 += 1

p1 = n1 / numbers * 100
p2 = n2 / numbers * 100
p3 = n3 / numbers * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
