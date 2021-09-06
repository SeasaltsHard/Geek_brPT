with open('text2.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for index, value in enumerate(lines, 1):
        word_numb = len(value.split())
        print(f'В строке {index} всего {word_numb} слов!')
        