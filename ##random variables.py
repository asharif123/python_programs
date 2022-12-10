##random variables
import random
##generate random value between 0 and 1
for i in range(3):
    print(random.random())

##random value from 10 to 20
for i in range(3):
    print(random.randint(10,20))

#select random team member
members = ['John','Mary','Bob','Mosh']
print(random.choice(members))

##create a class called Dice to randomly roll 2 die
##have roll method to return tuple of 2 random values

class Dice:
    def __init__(self):
        pass

    def roll(self):
        result = (random.randint(1,6), random.randint(1,6))
        return result

total = Dice()
print(total.roll())
