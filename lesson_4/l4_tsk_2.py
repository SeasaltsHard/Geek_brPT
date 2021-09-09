from random import randint
formed_list = [randint(0, 1250) for _ in range(randint(5, 15))]
target_list = [num for i, num in enumerate(formed_list[1:]) if num > formed_list[i]]

print(formed_list)
print(target_list)
