from math import floor
income = float(input())
gpa = float(input())
min_salary = float(input())

social_scholarship = 0
gpa_scholarship = 0

if income < min_salary and gpa > 4.5:
    social_scholarship = 0.35 * min_salary
if gpa >= 5.5:
    gpa_scholarship = gpa * 25

if gpa_scholarship >= social_scholarship:
    if social_scholarship == gpa_scholarship:
        print('You cannot get a scholarship!')
    else:
        print(f'You get a scholarship for excellent results {floor(gpa_scholarship)} BGN')
elif social_scholarship > gpa_scholarship:
    print(f'You get a Social scholarship {floor(social_scholarship)} BGN')