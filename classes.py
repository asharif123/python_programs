##class

##A class inherits from the class named object to make a class
##assume that Python always requires (object) when you make a class
class Animal(object):
    pass


##Dog class is inherited from Animal
class Dog(Animal):
    def __init__(self,name):
        self.name = name


class Cat(Animal):
    def __init__(self,name):
        self.name = name

class Person(object):
    def __init__(self,name):
        self.name = name

        ##person has some kind of pet
        self.pet = None

class Employee(Person):
    def __init__(self,name,salary):
##used to inherit attributes from parent class
#That’s how you can run the __init__ method of a parent class reliably.
        super(Employee,self).__init__(name)
        self.salary = salary


class Fish(object):
    pass

frank = Employee('Frank',120000)
print(frank.name)

fido = Dog("fido")
print(fido.name)