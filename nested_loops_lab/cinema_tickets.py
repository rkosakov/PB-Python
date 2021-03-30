command = input()
capacity = int(input())
total_tickets = 0
total_standard = 0
total_kid = 0
total_student = 0
while command != 'Finish':
    type_of_movie = input()
    total_for_movie = 0
    while type_of_movie != 'End':
        total_tickets += 1
        total_for_movie += 1
        if type_of_movie == 'student':
            total_student += 1
        elif type_of_movie == 'standard':
            total_standard += 1
        elif type_of_movie == 'kid':
            total_kid += 1
        if total_for_movie == capacity:
            break
        type_of_movie = input()
    print(f'{command} - {((total_for_movie / capacity) * 100):.2f}% full.')
    command = input()
    if command != 'Finish':
        capacity = int(input())
print(f'Total tickets: {total_tickets}')
print(f'{(total_student / total_tickets) * 100:.2f}% student tickets.')
print(f'{(total_standard/ total_tickets) * 100:.2f}% standard tickets.')
print(f'{(total_kid / total_tickets) * 100:.2f}% kids tickets.')