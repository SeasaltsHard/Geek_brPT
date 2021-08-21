# Задание №3
n = (input("Введите число "))
while n < '0':
    print('Число должно быть положительным!')
    n = (input('Пожалуйста, введите положительное число: '))
    continue
nn = int(n + n)
nnn = int(n + n + n)
n2 = int(n)
print(nn + nnn + n2)
