##inheritance
##ex: class Foo(Bar) makes a class Foo that inherits from the parent Bar

##implicit inheritance defi ne a function in the parent,but not in the child
class Parent(object):
    def implicit(self):
        print("Parent implicit()")

#child class inherits from parent   
#empty class that will inherit everything from parent class
class Child(Parent):
    pass

# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()

##override explicitly where you override the child function
class Parent(object):

    def override(self):
        print("Parent override()")

class Child(Parent):
    def override(self):
        print("Child override()")

# dad = Parent()
# son = Child()
# dad.override()
# son.override()

##Alter before or after You fi rst override the function just like in the You fi rst override the function just like in the last example, but then you use a Python built- in function named super to get the Parent versionto call.

# class Parent(object):
#     def altered(self):
#         print("Parent altered!")

# class Child(Parent):
#     def altered(self):
#         print("Child, before parent altered()")

#     super(Child, self).altered()
#     print("Child AFTER parent altered()")

##practice
class Parent(object):
    def override(self):
        print("Parent override()")

    def implicit(self):
        print("Parent implicit()")

    def altered(self):
        print("Parent altered()")

class Child(Parent):
    def override(self):
        print("Child override")

    def altered(self):
        print("CHILD, before parent altered()")
        #uses super to access altered() method from Parent class
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

    dad = Parent()
    son = Child()
    
    # ##parent implicit
    # dad.implicit()

    # ##parent implicit
    # son.implicit()

    # #parent override
    # dad.override()

    # #child override
    # son.override()

    # #parent altered()
    # dad.altered()

    # #child before parent altered
    # #parent altered()
    # #child after parent altered
    # son.altered()


#COMPOSITION  use other classes and modules
class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        #call the implicit method from other class
        self.other.implicit()

    def override(self):
        print("Child override()")

    def altered(self):
        print("CHILD BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD AFTER OTHER altered()")

son = Child()
#prints "OTHER implicit()"
son.implicit()
#prints "Child override()"
son.override()
#prints:
#CHILD BEFORE OTHER altered()
#OTHER altered()
#CHILD AFTER OTHER altered()
son.altered()