from math import pi, pow
figure = input()

area = 0
if figure == 'square':
    side = float(input())
    area = pow(side, 2)
elif figure == 'rectangle':
    side_1 = float(input())
    side_2 = float(input())
    area = side_1 * side_2
elif figure == 'circle':
    r = float(input())
    area = pi * pow(r, 2)
elif figure == 'triangle':
    length = float(input())
    height = float(input())
    area = (length * height) / 2

print(f'{area:.3f}')
