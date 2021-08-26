while True:
    expression = input('math:')
    if expression == 'q':
        exit()
    print(eval(expression))