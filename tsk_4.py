# Задание №4
text = input('Введите предложение из нескольких слов: ')
for x, line in enumerate(text.split()):
    x = f'{x + 1})'
    print(f'{x}{line[:10]}')
