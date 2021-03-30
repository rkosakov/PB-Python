favorite_book = input()
book = input()

counter = 0
while book != 'No More Books':

    if book == favorite_book:
        print(f'You checked {counter} books and found it.')
        exit(0)
    counter += 1
    book = input()

print('The book you search is not here!')
print(f'You checked {counter} books.')
