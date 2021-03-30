number_of_fails = int(input())
problem = input()
counter = 0
total_sum = 0
last_problem = ''
counter_fail = 0

while problem != 'Enough':
    grade = float(input())
    counter += 1
    last_problem = problem
    total_sum += grade
    if grade <= 4.00:
        counter_fail += 1
    if counter_fail == number_of_fails:
        print(f'You need a break, {number_of_fails} poor grades.')
        exit(0)

    problem = input()

average = total_sum / counter
print(f'Average score: {average:.2f}')
print(f'Number of problems: {counter}')
print(f'Last problem: {last_problem}')