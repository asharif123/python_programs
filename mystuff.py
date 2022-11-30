#import mystuff
def apple():
    print("I AM APPLES!")

#import mystuff
import mystuff

#A class is a way to take a grouping of functions and data and place
#them inside a container so you can access them with the '.' (dot) operator

class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print("I AM CLASSY APPLES!")

# stuff = MyStuff()
# stuff.apple()
# print(stuff.tangerine)

##Song class
class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

happy_bday.sing_me_a_song()

# bulls_on_parade = Song(["They rally around the family",
# "With pockets full of shells"])

# bulls_on_parade.sing_me_a_song()

##terms
#  • class—Tell Python to make a new kind of thing.
#  • object—Two meanings: the most basic kind of thing, and any instance of some thing.
#  • instance—What you get when you tell Python to create a class.
#  • def—How you defi ne a function inside a class.
#  • self—Inside the functions in a class, self is a variable for the instance/object being accessed.
#  • inheritance—The concept that one class can inherit traits from another class, much like
# you and your parents.
#  • composition—The concept that a class can be composed of other classes as parts, much
# like how a car has wheels.
#  • attribute—A property classes have that are from composition and are usually variables.
#  • is- a—A phrase to say that something inherits from another, as in a “salmon” is- a “fi sh.”
#  • has- a—A phrase to say that something is composed of other things or has a trait, as in “a
# salmon has- a mouth.”