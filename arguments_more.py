from sys import argv
script, filename = argv
##create a new text file by opening filename and add lines to the filename!

print("Script name", filename)

raw_input = ("?")
print("Opening file")
target = open(filename, 'w')

print("Truncating the file...")
print(target.truncate())

##add info to the file
print("I am going to ask your 3 lines!")
print("Line 1")
target.write('Line 1')
target.write("\n")

print("Line 2")
target.write('Line 2')
target.write("\n")

print("CLOSING!")
target.close()

