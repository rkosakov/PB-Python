number_tabs = int(input())
salary = int(input())
flag = False
for i in range(number_tabs):
    tab = input()
    if tab == 'Facebook':
        salary -= 150
    elif tab == 'Instagram':
        salary -= 100
    elif tab == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        flag = True
        break

if not flag:
    print(f'{salary}')