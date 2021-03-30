num_1 = int(input())
num_2 = int(input())
operator = input()

result = 0
even_odd = ''
flag = False
if operator == '+':
    result = num_1 + num_2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
elif operator == '-':
    result = num_1 - num_2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
elif operator == '*':
    result = num_1 * num_2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
elif operator == '/':
    if num_2 == 0:
        print(f'Cannot divide {num_1} by zero')
        flag = True
    else:
        result = num_1 / num_2
elif operator == '%':
    if num_2 == 0:
        print(f'Cannot divide {num_1} by zero')
        flag = True
    else:
        result = num_1 % num_2

if operator == '+' or operator == '-' or operator == '*':
    print(f'{num_1} {operator} {num_2} = {result} - {even_odd}')
elif not flag and operator == '/':
    print(f'{num_1} {operator} {num_2} = {result:.2f}')
elif not flag and operator == '%':
    print(f'{num_1} {operator} {num_2} = {result}')
