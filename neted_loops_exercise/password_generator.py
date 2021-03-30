num = int(input())
letter = int(input())

for i in range(1, num + 1):
    for j in range(1, num + 1):
        for k in range(letter):
            for l in range(letter):
                for m in range(1, num + 1):
                    if m > i and m > j:
                        print(f'{i}{j}{chr(97 + k)}{chr(97 + l)}{m}', end=' ')
