from sys import maxsize

nums = int(input())
even_sum = 0
even_min = maxsize
even_max = -maxsize
odd_sum = 0
odd_min = maxsize
odd_max = -maxsize
for i in range(1, nums + 1):
    number = float(input())
    if i % 2 == 0:
        even_sum += number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number
    elif i % 2 != 0:
        odd_sum += number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number

print(f'OddSum={odd_sum:.2f},')
if odd_min == maxsize:
    print('OddMin=No,')
else:
    print(f'OddMin={odd_min:.2f},')
if odd_max == -maxsize:
    print('OddMax=No,')
else:
    print(f'OddMax={odd_max:.2f},')
print(f'EvenSum={even_sum:.2f},')
if even_min == maxsize:
    print('EvenMin=No,')
else:
    print(f'EvenMin={even_min:.2f},')

if even_max == -maxsize:
    print('EvenMax=No')
else:
    print(f'EvenMax={even_max:.2f}')
