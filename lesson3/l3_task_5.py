def inf_add():
    total = 0
    while True:
        t_list = input('Enter a number to add. "Q" to exit').split()
        for i in t_list:
            if i == 'Q':
                return total
            else:
                try:
                    total += int(i)
                except ValueError:
                    print('Enter a number to add. "Q" to exit')
        print(f'Sum of numbers = {total}')


print(inf_add())
