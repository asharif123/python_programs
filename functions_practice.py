def add(a, b):
    print ("ADDING %s and %s" %(a,b))
    return a + b
age = add(3,5)
print(age)

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    print("Dividing %s/%s" %(a,b))
    return int(a/b)
numbers = divide(15,5)
print(numbers)