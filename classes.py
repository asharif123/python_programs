##class

##A class inherits from the class named object to make a class
##assume that Python always requires (object) when you make a class

class Point:
    #consttuctor, use init method to initialize our objects
    def __init__(self,x,y):
        #references current object
        self.x = x
        self.y = y

    def move(self):
        print("Moved!")

    def draw(self):
        print("Draw!")

point1 = Point(10,20)
print(point1.x)
print(point1.y)
point1.draw()
point1.move()


##define person object having name attribute and talk method
class Person:
    def __init__(self,name):
        self.name = name
    
    def talk(self):
        print("My name is %s!" %(self.name))

awad = Person("Awad")
print(awad.name)
awad.talk()

#diff object of instance from point 1
# point2 = Point()

# class Animal(object):
#     pass


# ##Dog class is inherited from Animal
# class Dog(Animal):
#     def __init__(self,name):
#         self.name = name


# class Cat(Animal):
#     def __init__(self,name):
#         self.name = name

# class Person(object):
#     def __init__(self,name):
#         self.name = name

#         ##person has some kind of pet
#         self.pet = None

# class Employee(Person):
#     def __init__(self,name,salary):
# ##used to inherit attributes from parent class
# #That’s how you can run the __init__ method of a parent class reliably.
#         super(Employee,self).__init__(name)
#         self.salary = salary


# class Fish(object):
#     pass

# frank = Employee('Frank',120000)
# print(frank.name)

# fido = Dog("fido")
# print(fido.name)


###Inheritance
class Mammal:
    def walk(self):
        print("walk")

#Dog inherits from Mammal
class Dog(Mammal):
    def bark(self):
        print("Woof!")


class Cat(Mammal):
    pass

#dog inherits from Mammal class
dog1 = Dog()
dog1.walk()
dog1.bark()
