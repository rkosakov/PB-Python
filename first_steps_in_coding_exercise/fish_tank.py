length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume = length * width * height
liters = volume / 1000
liters_needed = liters * (1 - (percentage / 100))
print(liters_needed)