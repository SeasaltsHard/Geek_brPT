from random import randint

with open('text5', 'w', encoding='utf-8') as n_file:
    my_list = [randint(1, 100) for _ in range(100)]
    n_file.write(' '.join(map(str, my_list)))

print(f'Sum of numbers = {sum(my_list)}')
