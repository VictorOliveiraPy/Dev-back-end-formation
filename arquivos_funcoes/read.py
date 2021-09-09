content = []

text = []

with open(file='../LICENSE', mode='r', encoding='utf8') as f:
    # content = f.read()
    line = f.readline()  # read first line
    while line:
        separate_line = line.split(sep=',')
        first_line = separate_line[0]
        text.append(first_line)
        line = f.readline()  # read a new line, if not exists line, saved value none

    print(content)
