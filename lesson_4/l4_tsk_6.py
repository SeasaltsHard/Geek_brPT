from itertools import count, cycle

my_cou = count(10)
my_cyc = cycle('SPAM!!!')
for i in range(15):
    print('Count, cycle = ({},{})'.format(next(my_cou), next(my_cyc)))
    