nums_input = int(input())
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0


for i in range(nums_input):
    number = int(input())
    if number < 200:
        n1 += 1

    elif 200 <= number <= 399:
        n2 += 1

    elif 400 <= number <= 599:
        n3 += 1

    elif 600 <= number <= 799:
        n4 += 1

    elif number >= 800:
        n5 += 1

p1 = n1 / nums_input * 100
p2 = n2 / nums_input * 100
p3 = n3 / nums_input * 100
p4 = n4 / nums_input * 100
p5 = n5 / nums_input * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
