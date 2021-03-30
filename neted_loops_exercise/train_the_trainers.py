number_judges = int(input())
text = input()
counter = 0
total_average = 0

while text != 'Finish':

    sum_grades = 0
    for i in range(1, number_judges + 1):
        grade = float(input())
        sum_grades += grade
    average = sum_grades / number_judges
    counter += 1
    total_average += average
    print(f'{text} - {average:.2f}.')
    text = input()

print(f"Student's final assessment is {(total_average / counter):.2f}.")

