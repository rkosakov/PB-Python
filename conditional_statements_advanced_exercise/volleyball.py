from math import floor

year = input()
holidays = int(input())
weekends = int(input())

saturdays_playing = 3/4 * (48 - weekends)
holidays_playing = holidays * 2/3
total_play = saturdays_playing + weekends + holidays_playing

if year == 'leap':
    total_play += total_play * 0.15
print(floor(total_play))