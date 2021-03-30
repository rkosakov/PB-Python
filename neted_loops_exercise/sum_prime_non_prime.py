text = input()

prime_sum = 0
composite_sum = 0

while text != 'stop':
    num = int(text)
    if num < 0:
        print(f'Number is negative.')
        text = input()
        continue
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter > 2:
        composite_sum += num
    else:
        prime_sum += num
    text = input()
print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {composite_sum}')