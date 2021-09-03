from sys import argv


def salary():
    try:
        hours, per_hour, bonus = map(float, argv[1:])
        print(f'Salary = {hours * per_hour + bonus}')
    except ValueError:
        print('3 numbers required!')


salary()
