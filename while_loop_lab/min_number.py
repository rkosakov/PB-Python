from sys import maxsize

text = input()
min_num = maxsize

while text != 'Stop':
    number = int(text)
    if number < min_num:
        min_num = number
    text = input()
print(min_num)