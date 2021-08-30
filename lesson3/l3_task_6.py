def int_func(word):
    letter = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(letter) else False


sent = input('Enter a sentence with lower letters: ').split()
for w in sent:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')
