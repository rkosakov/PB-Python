record = float(input())
distance = float(input())
time_for_a_meter = float(input())

delay = distance // 15
total_time = delay * 12.5 + distance * time_for_a_meter

if record > total_time:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {total_time - record:.2f} seconds slower.')