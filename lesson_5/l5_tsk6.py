my_dict = {}
with open('text7.txt', encoding='utf-8') as link:
    for line in link:
        name, stats = line.split(':')
        summa = sum(map(int, ''.join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        my_dict[name] = summa
print(f'{my_dict}')
