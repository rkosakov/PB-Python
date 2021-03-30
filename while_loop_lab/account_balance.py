text = input()
total = 0

while text != 'NoMoreMoney':
    number = float(text)
    if number < 0:
        print('Invalid operation!')
        print(f'Total: {total:.2f}')
        exit(0)
    else:
        total += number
        print(f'Increase: {number:.2f}')

    text = input()
print(f'Total: {total:.2f}')