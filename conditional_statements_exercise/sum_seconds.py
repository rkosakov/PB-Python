first = int(input())
second = int(input())
third = int(input())

sum_of_seconds = first + second + third
minutes = sum_of_seconds // 60
seconds = sum_of_seconds % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
