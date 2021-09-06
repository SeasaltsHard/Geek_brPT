with open('text3.txt', encoding='utf-8') as fd:
    emp_dict = {line.split()[0]: float(line.split()[1]) for line in fd}
    print(f'Average salary: {round(sum(emp_dict.values())/ len(emp_dict), 3)})\n'
          f'Lowest income employees:{[i[0] for i in emp_dict.items() if i[1] < 20000]}')
