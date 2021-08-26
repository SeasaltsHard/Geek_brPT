# Задание №3
# С применением списка:
a = int(input('"List": Enter the month number (1-12): '))
b = ('Winter', 'Spring', 'Summer', 'Autumn')
if 12 == a or a <= 2:
    print(b[0])
elif 3 <= a < 6:
    print(b[1])
elif 6 <= a < 9:
    print(b[2])
else:
    print(b[3])
# С применением словаря:
Months = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
          5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October',
          11: 'November', 12: 'December'}
c = int(input('"Dict": Enter the month number (1-12): '))
print(Months.get(c))
