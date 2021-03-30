time = int(input())
day = input()

is_working_day = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday'
is_working_time = 10 <= time <= 18

if is_working_time and is_working_day:
    print('open')
else:
    print('closed')
