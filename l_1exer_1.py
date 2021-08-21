# Задание №1
n_1 = int(input("Введите первое число "))
print("Ваше число: ", n_1)
n_2 = int(input("Введите второе число "))
print("Ваше число: ", n_2)
action = input("(Введите действие (pl, mns, div, mlt)")
if action == "pl":
    print(n_1 + n_2)
elif action == "mns":
    print(n_1 - n_2)
elif action == "div":
    print(n_1 / n_2)
elif action == "mlt":
    print(n_1 * n_2)
else:
    print('Вы ввели недопустимое действие')


