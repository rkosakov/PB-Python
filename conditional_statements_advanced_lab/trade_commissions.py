city = input()
sales = float(input())
percentage = 0
flag = False
if city == 'Sofia':
    if 0 <= sales <= 500:
        percentage = 0.05
    elif 500 < sales <= 1000:
        percentage = 0.07
    elif 1000 < sales <= 10000:
        percentage = 0.08
    elif sales > 10000:
        percentage = 0.12
    else:
        print('error')
        flag = True
elif city == 'Varna':
    if 0 <= sales <= 500:
        percentage = 0.045
    elif 500 < sales <= 1000:
        percentage = 0.075
    elif 1000 < sales <= 10000:
        percentage = 0.10
    elif sales > 10000:
        percentage = 0.13
    else:
        print('error')
        flag = True
elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        percentage = 0.055
    elif 500 < sales <= 1000:
        percentage = 0.08
    elif 1000 < sales <= 10000:
        percentage = 0.12
    elif sales > 10000:
        percentage = 0.145
    else:
        print('error')
        flag = True
else:
    print('error')
    flag = True

if not flag:
    print(f'{sales * percentage:.2f}')
