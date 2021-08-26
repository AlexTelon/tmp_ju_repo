import random

guess = input('guess number between 0 and 10\n')
secret = random.choice(range(0, 11))

if guess == secret:
    print('win!')
else:
    print('lose :(')
    print(f'Correct was {secret}')