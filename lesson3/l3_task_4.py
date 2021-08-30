# С помощью '**'
def my_func(x, y):
    try:
        s = x ** y
    except TypeError:
        return print('Positive and negative numbers only')
    return s


print(my_func(21, -4))


# Без помощи '**'
def my_func_c(f, z):
    try:
        f, z = float(f), int(z)
        if f <= 0 or z >= 0:
            return '"f" must be < 0; "z" must be < 0.'
        else:
            result = 1
            for i in range(abs(z)):
                result /= f
            return f'"f" in power of "z" is: {round(result, 6)}'
    except ValueError:
        print('Numbers only allowed!')


n_1 = (input('Enter first, positive number: '))
n_2 = (input('Enter second, negative number: '))

print(my_func_c(n_1, n_2))
