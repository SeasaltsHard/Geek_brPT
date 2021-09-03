def factorials(num):
    start = 1
    for i in range(num + 1):
        yield f'{i}! = {start}'
        start *= i + 1


for x in factorials(int(input('Factorial number: '))):
    print(x)
