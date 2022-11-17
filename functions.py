##functions
# def print_two(*args):
#     arg1,arg2 = args
#     print("Arguments: %s, %s" %(arg1,arg2))
# print_two(1,2)

# def cheese_and_crackers(cheese_count, crackers_count):
#     print ("You have %s cheese" %(cheese_count))
#     print ("You have %s crackers " %(crackers_count))

# cheese_and_crackers(6,10)

from sys import argv

script, input_file = argv
def print_all(f):
    
    print (f.read())

def rewind(f):
    f.seek(0)
#need to open the file before you can read it!
current_file = open(input_file)

#function reads it line by line
def print_a_line(line_count,f):
    print(line_count, f.readline())

print("First print the whote file\n")
print_all(current_file)

#rewind a file
print("Now let us rewind")
rewind(current_file)

#print 2 lines
print("Let us print 3 lines")
print_a_line(1,current_file)
print_a_line(2,current_file)
print_a_line(3,current_file)