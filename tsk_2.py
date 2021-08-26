# Задание №2:
a = list(input(' '))
for i in range(1, len(a), 2):
    a[i], a[i - 1] = a[i - 1], a[i]
print(a)
