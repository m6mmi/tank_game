# create a simple map to display tank and target
def target_symbol():
    print(u'\u2622')


def tank_up():
    return u'\u25B3'


def tank_down():
    return u'\u25BD'


def tank_left():
    return u'\u25C1'


def tank_right():
    return u'\u25B7'


def draw_map(tank_x, tank_y, tank_direction):
    global vertical, tank_symbol
    matrix = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

    horizontal = tank_x + 5
    if tank_y >= 0:
        vertical = -abs(tank_y) + 5
    elif tank_y < 0:
        vertical = abs(tank_y) + 5

    if tank_direction == 'up':
        tank_symbol = tank_up()
    elif tank_direction == 'down':
        tank_symbol = tank_down()
    elif tank_direction == 'left':
        tank_symbol = tank_left()
    elif tank_direction == 'right':
        tank_symbol = tank_right()

    matrix[vertical][horizontal] = tank_symbol

    for i in matrix:
        for j in i:
            print(j, end="  ")
        print()



