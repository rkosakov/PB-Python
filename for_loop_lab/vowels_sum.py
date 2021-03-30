text = input()

sum_of_vowels = 0

for symbol in text:
    if symbol == 'a':
        sum_of_vowels += 1
    elif symbol == 'e':
        sum_of_vowels += 2
    elif symbol == 'i':
        sum_of_vowels += 3
    elif symbol == 'o':
        sum_of_vowels += 4
    elif symbol == 'u':
        sum_of_vowels += 5
print(sum_of_vowels)