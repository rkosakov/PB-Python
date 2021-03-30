width = int(input())
length = int(input())
height = int(input())
text = input()

volume = width * length * height
total_boxes = 0
while text != 'Done':
    boxes = int(text)
    total_boxes += boxes
    if total_boxes > volume:
        print(f'No more free space! You need {total_boxes - volume} Cubic meters more.')
        exit(0)

    text = input()
print(f'{volume - total_boxes} Cubic meters left.')
