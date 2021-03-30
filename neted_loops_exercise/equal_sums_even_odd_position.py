start = int(input())
end = int(input())

for i in range(start, end + 1):

    first = i // 100000
    second = i // 10000 % 10
    third = i // 1000 % 10
    forth = i // 100 % 10
    fifth = i // 10 % 10
    sixth = i % 10
    even_sum = second + forth + sixth
    odd_sum = first + third + fifth
    if even_sum == odd_sum:
        print(str(i) + ' ', end='')


