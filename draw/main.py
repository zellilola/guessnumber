def print_x():
    print('X ', end='')


def print_space():
    print('  ', end='')


def is_on_border(x, y):
    return (x == 0 or x == matrix_size - 1) or (y == 0 or y == matrix_size - 1)


def is_on_cross(x, y):
    return x == y or (x + y) == matrix_size - 1


matrix_size = 5
for x in range(matrix_size):
    for y in range(matrix_size):
        if not is_on_border(x, y) and not is_on_cross(x, y):
            print_space()
            continue

        print_x()

    print('')
