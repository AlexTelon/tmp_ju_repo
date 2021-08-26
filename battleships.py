from collections import defaultdict

field = defaultdict(list)

for y in range(10):
    for x in range(10):
        field[y].append('~')


for k, value in field.items():
    print("".join(value))
