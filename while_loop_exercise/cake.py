width = int(input())
height = int(input())

total_pieces = width * height
text_input = input()

while text_input != 'STOP':
    piece = int(text_input)
    total_pieces -= piece
    if total_pieces <= 0:
        print(f'No more cake left! You need {abs(total_pieces)} pieces more.')
        exit(0)
    text_input = input()
print(f'{total_pieces} pieces are left.')
