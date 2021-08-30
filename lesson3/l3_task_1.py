def my_div():
    f_arg = int(input("Укажите первое число: "))
    s_arg = int(input("Укажите второе: "))
    try:
        div_res = f_arg // s_arg
    except ZeroDivisionError:
        print('Нельзя делить на 0!')
    else:
        return print(div_res)


my_div()
