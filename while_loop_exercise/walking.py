text_input = input()
total_steps = 0
while text_input != 'Going home':
    steps = int(text_input)
    total_steps += steps

    if total_steps >= 10000:
        print('Goal reached! Good job!')
        print(f'{total_steps - 10000} steps over the goal!')
        exit(0)
    text_input = input()
steps_after = int(input())
total_steps += steps_after
if total_steps >= 10000:
    print('Goal reached! Good job!')
    print(f'{total_steps - 10000} steps over the goal!')
else:
    print(f'{10000 - total_steps} more steps to reach goal.')