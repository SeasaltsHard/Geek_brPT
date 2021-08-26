# Задание №5
num_list = [5, 5, 5, 4, 2, 1]
new_num = (int(input("Введите новое число: ")))
x = 0
for i in num_list:
    if new_num <= i:
        x += 1
    else:
        break
num_list.insert(x, new_num)
print(num_list)
