##functions
def print_two(*args):
    arg1,arg2 = args
    print("Arguments: %s, %s" %(arg1,arg2))
print_two(1,2)

def cheese_and_crackers(cheese_count, crackers_count):
    print ("You have %s cheese" %(cheese_count))
    print ("You have %s crackers " %(crackers_count))

cheese_and_crackers(6,10)