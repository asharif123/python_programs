# people = 20
# cars = 40
# buses = 16
# if cars > people:
#     print("we should take the cars")
# elif cars < people:
#     print("We should not take the cars")
# else:
#     print("We can't decide")

print("You enter a dark room! Choose either door 1 or door #2!")
door = input("")
if door == "1":
    print("There is a giant bear! What do you do?")
    print("1. Attack")
    print("2. Scream and run")
    bear = input("")
    if bear == "1":
        print("You are dead!")
    elif bear == "2":
        print("You are alive!")
    else:
        print("Good job! %s is the best option!" %(bear))

elif door == "2":
    print("What is it gonna be?")
    print("1. Blueberries")
    print("2. Yellow jacket")
    print("3. Others")
    insanity = input("")
    if (insanity == "1" or insanity =="2"):
        print("You survived!")
    else:
        print("You are dead!")


else:
    print("You made it out!")