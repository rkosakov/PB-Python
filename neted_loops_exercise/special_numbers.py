num = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                is_special = num % i == 0 and num % j == 0 and num % k == 0 and num % l == 0
                if is_special:
                    print(f'{i}{j}{k}{l}', end=' ')
