from sys import exit

def gold_room():
    print("This room is full of gold how much do you take?")
    how_much = int(input(""))


    if how_much < 50:
        print("Nice you are not greedy!")
        exit(0)
    else:
        print("You are greedy!")


def bear_room():
    print("How are you going to move the bear?")
    bear_moved = False
    while True:
        next = input("")
        if next == "take honey":
            print("The bear will slap you!")
##if next == taunt and not bear_moved (True)
        elif next == "taunt" and not bear_moved:
            print(bear_moved)
            print("The bear has moved you can go through!")
            bear_moved = True
        elif next == "taunt" and bear_moved:
            print("The bear is going to attack you!")
        elif next == "open" and bear_moved:
            print(bear_moved)
            gold_room()
        else:
            print("Invalid input!")



#respond to whatever decision user makes
def start():
    print("You are in a dark room!")
    print("Select either a door from the left or right")
    decision = input("")
    if decision == "left":
        bear_room()
    else:
        print("You failed!")

start()

