from random import randint
import main_functions as fns

directions = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}


class Tank:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'up'

    def __str__(self):
        return f"Current tank position is [{self.x}, {self.y}] and it is facing {self.direction}"

    def move(self, direction):
        if direction in directions.values():
            if direction == 'up':
                if self.y < 5:
                    self.y += 1
                else:
                    print("Coordinate can not be more than 5")
            elif direction == 'down':
                if self.y > -5:
                    self.y -= 1
                else:
                    print("Coordinate can not be less than -5")
            elif direction == 'right':
                if self.x < 5:
                    self.x += 1
                else:
                    print("Coordinate can not be more than 5")
            elif direction == 'left':
                if self.x > -5:
                    self.x -= 1
                else:
                    print("Coordinate can not be less than -5")
            self.direction = direction
        else:
            print("Not present")

    def shoot(self, target_x, target_y):
        if self.direction == 'up' or self.direction == 'down':
            if target_x == self.x:
                if target_y > self.y and self.direction == 'up':
                    return True
                if target_y < self.y and self.direction == 'down':
                    return True

        return True


class Target:
    def __init__(self):
        self.x = randint(-5, 5)
        self.y = randint(-5, 5)

    def reset(self):
        self.x = randint(-5, 5)
        self.y = randint(-5, 5)

    def __str__(self):
        return f"Target coordinates are [{self.x}, {self.y}]"


tank = Tank()
target = Target()

# Making sure that tank and target don't have same coordinates
while tank.x == target.x and tank.y == target.y:
    target.reset()

main_actions = fns.initial_user_input()
if main_actions == '1':
    print("Welcome to the tank game, lets GO !!")
    while True:
        tank_move = fns.tm_input()
        if tank_move == 't':
            if tank.shoot(target.x, target.y):
                target.reset()
            else:
                print("Missed the target")

        tank.move(directions[tank_move])
        print(tank)
        print(target)
elif main_actions == '2':
    print(f'Previous result')
elif main_actions == '3':
    print('Getting username')
    print('Saving high score')


