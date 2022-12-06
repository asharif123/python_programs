# ##while
# i = 1
# while i <= 5:
#     #prints: *, **, ***, ****, *****
#     print('*'*i)
#     i += 1
# #prints 6
# print(i)

##guess a number
# secret_number= 9
# count = 3

# while count > 0:
#     guess = int(input('Guess: '))
#     count -= 1
#     if guess == secret_number:
#         print("SUCCESS!")
#         break
#     else:
#         print("\nIncorrect. You have %s guesses left!" %(count))

##car game
##user should not start or stop it multiple times!
is_started = False
# is_stopped = True
while True:
    decision = input('')
    if decision.upper() == 'START' and is_started:
        print("\nCar has already started!")
    elif decision.upper() == 'STOP' and not is_started:
        print("\nCar has already stopped!")
    elif decision.upper() == 'START':
        print("\nStarting the car!")
        is_started = True
    elif decision.upper() == 'STOP':
        print("\nStopping the car")
        is_started = False
    elif decision.upper() == "HELP":
        print("""
start - start the car
stop - stop the car
quit - exit the program
        """)
    elif decision.upper() == 'QUIT':
        print("\nQuitting the game!")
        break
    else:
        print("I do not understand this input!")
     