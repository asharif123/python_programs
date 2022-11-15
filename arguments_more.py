from sys import argv
script, filename = argv
##create a new text file by opening filename and add lines to the filename!

print("Script name", filename)

raw_input = ("?")
print("Opening file")
target = open(filename, 'w')

print("Truncating the file...")
#truncating empties the file


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

##copying 1 file to another
from sys import argv
from os.path import exists
script, from_file, to_file = argv
print("Copying from %s to %s" %(from_file, to_file))

in_file = open(from_file).read()

print("The input file is %s bytes long" %(len(in_file)))
out_file = open(to_file, 'w')
##.write() add contents to your file WITHOUT overwriting any content!
out_file.write(in_file)

out_file.close()
in_file.close()




