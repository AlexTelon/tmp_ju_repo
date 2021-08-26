from collections import defaultdict
import random

field = defaultdict(list)

ships = [1, 2, 4, 4, 6]

for y in range(10):
    for x in range(10):
        field[y].append('~')

for ship_length in ships:
    x = max(0, random.choice(range(10)) - ship_length)
    y = random.choice(range(10))

    for i in range(ship_length):
        field[y][x+i] = 'X'


for k, value in field.items():
    print("".join(value))
