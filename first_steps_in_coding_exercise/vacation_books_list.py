pages_in_a_book = int(input())
pages_per_hour = int(input())
days = int(input())
total_time = pages_in_a_book / pages_per_hour
hours_a_day = total_time / days
print(hours_a_day)
