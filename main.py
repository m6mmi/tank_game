from random import randint
import main_functions as fns
import map_grid
import json


directions = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}

with open('scores.txt', 'r+') as f:
    data = json.load(f)

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
        elif self.direction == 'left' or self.direction == 'right':
            if target_y == self.y:
                if target_x < self.x and self.direction == 'left':
                    return True
                if target_x > self.x and self.direction == 'right':
                    return True
        return False


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

# Making sure that tank and target don't have the same coordinates
while tank.x == target.x and tank.y == target.y:
    target.reset()



while True:
    score = 0
    target_count = 5
    match fns.initial_user_input():
        case "1":
            print("Welcome to the tank game, lets GO !!")
            print("Destroy 10 targets. Hit = 10p. Move = -1. Miss = -5.")
            while True:
                if target_count == 0:
                    print(f"Score: {score}")
                    name = input("Please enter your name: ")
                    data[name] = str(score)
                    break
                map_grid.draw_map(tank.x, tank.y, tank.direction, target.x, target.y)
                tank_move = fns.tm_input()
                if tank_move == 'f':
                    if tank.shoot(target.x, target.y):
                        target.reset()
                        print("\nHit !!! Target destroyed.")
                        score += 10
                        target_count -= 1
                    else:
                        print("\nMissed the target")
                        score -= 5
                elif tank_move == 'x':
                    break
                else:
                    tank.move(directions[tank_move])
                    score -= 1
        case "2":
            print(f'{"High Scores":-^20}')
            for key, value in data.items():
                print(f"{key + " -> " + value:^20}")
        case "3":
            print('Getting username')
            print('Saving high score')
            break

