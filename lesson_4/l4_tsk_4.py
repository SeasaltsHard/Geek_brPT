from random import randint
rand_list = [randint(1, 20) for _ in range(20)]
red_list = [i for i in rand_list if rand_list.count(i) == 1]
print(f'{rand_list}\n{red_list}')
