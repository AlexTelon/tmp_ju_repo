from collections import defaultdict
import random

field = defaultdict(list)

ships = [1, 2, 4, 4, 6]

for y in range(10):
    for x in range(10):
        field[y].append('~')

for ship_length in ships:
    horizontal = random.choice([True, False])

    x = random.choice(range(10))
    y = random.choice(range(10))

    # If the ship would end up outside the playing field
    # then move it back a bit so it will be inside.
    if horizontal and x + ship_length >= 10:
        x -= (x + ship_length - 10)
    if not horizontal and y + ship_length >= 10:
        y -= (y + ship_length - 10)

    for i in range(ship_length):
        if horizontal:
            field[y][x+i] = 'X'
        else:
            field[y+i][x] = 'X'



for k, value in field.items():
    print("".join(value))
