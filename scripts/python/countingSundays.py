def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day_of_week = 0

for year in range(1900, 1901):
    for month in range(12):
        if month == 1 and is_leap_year(year):
            day_of_week = (day_of_week + 29) % 7
        else:
            day_of_week = (day_of_week + month_days[month]) % 7

sundays_on_first = 0

for year in range(1901, 2001):
    for month in range(12):
        if day_of_week == 6:
            sundays_on_first += 1
        if month == 1 and is_leap_year(year):
            day_of_week = (day_of_week + 29) % 7
        else:
            day_of_week = (day_of_week + month_days[month]) % 7

print("Sundays on first:", sundays_on_first)
