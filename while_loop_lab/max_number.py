from sys import maxsize

text = input()
max_num = -maxsize
while text != 'Stop':
    number = int(text)
    if number > max_num:
        max_num = number
    text = input()
print(max_num)