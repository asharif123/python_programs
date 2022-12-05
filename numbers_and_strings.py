# print(3+2+1-5%4)
# print("What is 3+2?", 5)
# print("Is it greater than or equal to?", 3 >= 2)
# print("Is it less than or equal to?", 4 <= 16)

# #modulus division
# print(31 % 2)
# #round down
# print(33 // 4)

# #variables
# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# cars_not_driver = cars - drivers
# print ("There are", cars, "available!")
# average_passengers_per_car = passengers / drivers
#name = 'John Smith'
#age = 29
#is_new_patient = True

# #string formatting
# my_name = "Awad Sharif"
# my_age = 32
# my_height = 116
# my_weight = 180

# print("My weight is %s" %my_weight, "lbs!")

# print("My name is %s " %my_name)
# print("My age is %s" %my_age, "years old!")

# #decimal formating
# print("My height and weight are %d pounds and %d inches." %(my_height, my_weight))

# #combined sentences
# w = "This is the left side"
# e = "this is the right side!"

# print(w + e)

# #formatter
# formatter = "%s %s %s %s"
# print (formatter % ("one", "two", "three", "four"))

# #strings
# x = "There are %s types of people!" %(10)
# print(x)

# #newline
# months = "\nJan\nFeb\nMar\nApr"
# print("These are the months", months)

# print("I am 6\'2 tall!")
# #adds backslash between words!
# backslash_cat = "I'm \\ a \\ cat."
# print(backslash_cat)

##Escape What it does.
##\\ Backslash (\)
##\' Single- quote (')
##\" Double- quote (")
##\a ASCII bell (BEL)
##\b ASCII backspace (BS)
##\f ASCII formfeed (FF)
##\n ASCII linefeed (LF)
##\N{name} Character named name in the Unicode database (Unicode only)
##\r ASCII carriage return (CR)
##\t ASCII horizontal tab (TAB)

##taking user input

# print ("How old are you? ")
# age = input()
# print(age)
# print("How much do you weigh? ")
# weight = input()
# print(weight)
# print ("So you are %s years old and weigh %s lbs!" %(age, weight))

##parameters, arguments

# #holds arguments
# from sys import argv

##type conversion
# birth_year = input('Birth year: ')
# age = 2022 - int(birth_year)
# print(age)
# ##float() converts string in float
# ##bool converts string into boolean value
# ##type of variable
# print(type(birth_year))
weight = float(input("How much do you weight (in lbs)? "))
print("You weight: ", round(weight*0.454, 2), "kgs!")
sentence = ("Course for beginner\'s")

first_name = "Awad"
last_name = "Sharif"
##string formatting 
msg = f'{first_name + " " + last_name}'
print(msg)

