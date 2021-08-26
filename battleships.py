from collections import defaultdict
import random

hidden_field = defaultdict(list)
user_view = defaultdict(list)

ships = [1, 2, 4, 4, 6]

def print_field(field):
    for k, values in field.items():
        print(''.join(values))

# Create a hidden computer field.
for y in range(10):
    for x in range(10):
        hidden_field[y].append('~')

# Create a nice player visualisation of where they guessed.
for y in range(10):
    for x in range(10):
        user_view[y].append('~')

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
            hidden_field[y][x+i] = 'X'
        else:
            hidden_field[y+i][x] = 'X'


lives = 20
while lives > 0:
    print(f'You have {lives} guesses left')

    try:
        user_input = input('Guess a coodinate, eg 5 3 or q to quit\n')
        if user_input == 'q':
            exit()
        x,y = map(int, user_input.split(' '))
    except Exception as e:
        print('Something went wrong parsing your input {user_input}')
        print('please ensure to use "x y" format, like 5 4 for example.')
        continue

    if hidden_field[y][x] == 'X':
        print('hit!')
        user_view[y][x] = '#'
    else:
        print('miss!')
        lives -= 1
        user_view[y][x] = 'O'

    print_field(user_view)