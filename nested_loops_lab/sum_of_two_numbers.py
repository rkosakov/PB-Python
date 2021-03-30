start = int(input())
end = int(input())
result = int(input())

combination_counter = 0

for i in range(start, end + 1):
    for j in range(start, end + 1):
        combination_counter += 1
        if i + j == result:
            print(f'Combination N:{combination_counter} ({i} + {j} = {result})')
            exit(0)
print(f'{combination_counter} combinations - neither equals {result}')