from sys import maxsize
nums_number = int(input())
numbers_sum = 0
max_number = -maxsize

for i in range(0, nums_number):
    number = int(input())
    numbers_sum += number
    if number > max_number:
        max_number = number

numbers_sum -= max_number

if numbers_sum == max_number:
    print('Yes')
    print(f'Sum = {numbers_sum}')
else:
    print('No')
    print(f'Diff = {abs(numbers_sum - max_number)}')
