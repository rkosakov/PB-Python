inputs = int(input())

left_sum = 0
right_sum = 0
for i in range(inputs):
    nums = int(input())
    left_sum += nums

for j in range(inputs):
    numbers = int(input())
    right_sum += numbers

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')

