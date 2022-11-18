
from sys import argv

##run like this in the terminal: python3 arguments.py r s t

# script, first, second, third = argv

# print ("The script is called:", script)
# print ("Your first variable is:", first)
# print ("Your second variable is:", second)
# print ("Your third variable is:", third)

# # script, user_name = argv
# prompt = "<"
# # print("Hi, %s(). The script name is %s()" %(script, user_name))
# likes = input(prompt)
# print(likes)

##reading files
from sys import argv
# script, filename = argv
# txt = open(filename)
# print("Here is your file %s()" %(script))
# #read a file
# print(txt.read())
# #close the file
# txt.close()
script, filename = argv
print("The name of your file %s()" %(script))
print((open(filename)).read())
