with open('text.txt', 'w', encoding='utf-8') as l:
    while True:
        line = (input('Add data here: '))
        if not line:
            break
        print(line, file=l)
        