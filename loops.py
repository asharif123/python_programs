# ##while: used to execute a block of code multiple times
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

# #assume car has not started
# #change to true when user has started the car
# is_started = False

# while True:
#     decision = input('')
#     if decision.upper() == 'START' and is_started:
#         print("\nCar has already started!")
#     #if user enters stop and not is_started (not False = True)
#     elif decision.upper() == 'STOP' and not is_started:
#         print("\nCar has already stopped!")
#     elif decision.upper() == 'START':
#         print("\nStarting the car!")
#         is_started = True
#     elif decision.upper() == 'STOP':
#         print("\nStopping the car")
#         is_started = False
#     elif decision.upper() == "HELP":
#         print("""
# start - start the car
# stop - stop the car
# quit - exit the program
#         """)
#     elif decision.upper() == 'QUIT':
#         print("\nQuitting the game!")
#         break
#     else:
#         print("I do not understand this input!")


##for loop used to iterate over a finite resource
for item in 'Python':
    print(item)

for value in range(1,10, 2):
    print(value)

prices = [10,20,30]
total = 0
for value in prices:
    total += value
print("Total price: $",total)

##nested loop
for x in range(4):
    for y in range(3):
        print(f'{x},{y}')
#
##prints the following
##*****
##**
##*****
##**
##**

numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += ('x')
    print(output)

##print the following
## *
## *
## *
## *
## *
## *****
numbers = [1,1,1,1,1,5]
for count in numbers:
    output = ''
    for value in range(count):
        output += '*'
    print(output)