number = float(input())
input_num = input()
output_num = input()

converted = 0
if input_num == 'mm' and output_num == 'cm':
    converted = number / 10
elif input_num == 'mm' and output_num == 'm':
    converted = number / 1000
elif input_num == 'cm' and output_num == 'mm':
    converted = number * 10
elif input_num == 'cm' and output_num == 'm':
    converted = number / 100
elif input_num == 'm' and output_num == 'mm':
    converted = number * 1000
elif input_num == 'm' and output_num == 'cm':
    converted = number * 100

print(f'{converted:.3f}')