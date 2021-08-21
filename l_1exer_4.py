# Задание №4
num = int(input('Введите число'))
mxnum = num % 10
num = num // 10
while num > 0:
    if num % 10 > mxnum:
        mxnum = num % 10
    num = num // 10
print(mxnum)

