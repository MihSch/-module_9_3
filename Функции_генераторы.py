
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i) - len (j) for i, j in zip(first, second) if len(i) != len(j))
print(list(first_result))

second_res = (len(first[i]) == len(second[i]) for i in range(3))
print(list(second_res))