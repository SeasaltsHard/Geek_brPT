from functools import reduce


def the_list(el1, el2):
    return el1 * el2


da_list = [el for el in range(100, 1001, 2)]
print(da_list)
print(reduce(the_list, da_list))
      