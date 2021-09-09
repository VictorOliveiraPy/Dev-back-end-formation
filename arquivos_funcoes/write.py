ages = [11, 12, 14, 10]

""" write mode (w) overwrite """
with open(file='idades.Csv', mode='w', encoding='utf8') as f:
    line = 'age' + '\n'
    f.write(line)
    for age in ages:
        line = str(age) + '\n'
        f.write(line)

""" add mode (a) """

with open(file='idades.csv', mode='a', encoding='utf8') as f:
    for ages in ages:
        line = str(age + 100) + '\n'
        f.write(line)

"""copy between files """
with open(file='idades.csv', mode='r', encoding='utf8') as read_f:
    with open(file='idades.Csv', mode='w', encoding='utf8') as write_f:
        line = read_f.readline()
        while line:
            write_f.write(line)
            line = read_f.readline()
