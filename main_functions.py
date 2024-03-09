def initial_user_input():
    options = ["1", "2", "3"]
    while True:
        user_input = input("Choose your action form below:\n"
                           "1. Play the Game\n"
                           "2. See Results\n"
                           "3. Exit the Game\n"
                           ">>> ")

        if user_input in options:
            return user_input
        print(f"Please pic of the options {options}")


def tm_input():
    options = ["w", "s", "a", "d", "t"]
    while True:
        user_input = input("Choose where tank will go:\n"
                           "w > UP\n"
                           "s > DOWN\n"
                           "a > LEFT\n"
                           "d > RIGHT\n"
                           "F > FIRE !!!\n"
                           ">>> ")
        if user_input.lower() in options:
            return user_input.lower()
        print(f"Please pic of the options {options}")
