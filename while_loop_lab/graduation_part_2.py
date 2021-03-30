name = input()

counter = 0
total = 0
failures = 0
while counter != 12:
    grade = float(input())
    if grade >= 4.00:
        total += grade
        counter += 1
    else:
        failures += 1
    if failures == 2:
        print(f'{name} has been excluded at {counter + 1} grade')
        exit(0)
average = total / 12
print(f'{name} graduated. Average grade: {average:.2f}')
