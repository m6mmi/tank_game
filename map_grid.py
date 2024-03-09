# create a simple map to display tank and target
def target_symbol():
    return u'\u2622'


def tank_up():
    return u'\u25B3'


def tank_down():
    return u'\u25BD'


def tank_left():
    return u'\u25C1'


def tank_right():
    return u'\u25B7'


def draw_map(tank_x, tank_y, tank_direction, target_x, target_y):
    global vertical, tank_symbol, vertical_target
    matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    # Tank coordinates for matrix grid
    horizontal = tank_x + 5
    if tank_y >= 0:
        vertical = -abs(tank_y) + 5
    elif tank_y < 0:
        vertical = abs(tank_y) + 5

    # Tank facing a direction
    if tank_direction == 'up':
        tank_symbol = tank_up()
    elif tank_direction == 'down':
        tank_symbol = tank_down()
    elif tank_direction == 'left':
        tank_symbol = tank_left()
    elif tank_direction == 'right':
        tank_symbol = tank_right()

    # Insert tank symbol
    matrix[vertical][horizontal] = tank_symbol

    # get target coordinates
    horizontal_target = target_x + 5
    if target_y >= 0:
        vertical_target = -abs(target_y) + 5
    elif target_y < 0:
        vertical_target = abs(target_y) + 5

    # Insert target symbol
    matrix[vertical_target][horizontal_target] = target_symbol()

    # print matrix in console
    print(f"{'\u250F'}{'\u2501' * 33}{'\u2513'}")
    for i in matrix:
        print(u'\u2503', end=" ")
        for j in i:
            print(j, end="  ")
        print(u'\b\u2503')
    print(f"{'\u2517'}{'\u2501' * 33}{'\u251B'}")



