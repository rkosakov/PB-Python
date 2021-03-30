exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_in_minutes = exam_hour * 60 + exam_minutes
arrival_in_minutes = arrival_hour * 60 + arrival_minutes
difference = 0

if arrival_in_minutes > exam_in_minutes:
    print('Late')
    difference = arrival_in_minutes - exam_in_minutes
    if difference >= 60:
        hours_difference = difference // 60
        minutes_difference = difference % 60
        if minutes_difference < 10:
            print(f'{hours_difference}:0{minutes_difference} hours after the start')
        elif minutes_difference >= 10:
            print(f'{hours_difference}:{minutes_difference} hours after the start')
    else:
        print(f'{difference} minutes after the start')
elif exam_in_minutes - arrival_in_minutes <= 30:
    print('On time')
    if exam_in_minutes != arrival_in_minutes:
        minutes_early = abs(arrival_in_minutes - exam_in_minutes)
        print(f'{minutes_early} minutes before the start')
elif exam_in_minutes - arrival_in_minutes > 30:
    print('Early')
    difference = exam_in_minutes - arrival_in_minutes
    if difference >= 60:
        hours_difference = difference // 60
        minutes_difference = difference % 60
        if minutes_difference < 10:
            print(f'{hours_difference}:0{minutes_difference} hours before the start')
        elif minutes_difference >= 10:
            print(f'{hours_difference}:{minutes_difference} hours before the start')
    else:
        print(f'{difference} minutes before the start')

