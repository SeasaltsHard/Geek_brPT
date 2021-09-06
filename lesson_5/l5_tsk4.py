rus_eq = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('text5.txt', 'w', encoding='utf-8') as new_txt:
    with open('text4.txt', 'w', encoding='utf-8') as old_txt:
        new_txt.writelines([line.replace(line.split()[0], rus_eq.get(line.split()[0])) for line in old_txt])
