from helpers import options

def while_test (follow):
    while follow:
        choice = options()
        print(choice)
        print("hi")
        if choice == 5:
            follow = False
    return choice

while_test(True)