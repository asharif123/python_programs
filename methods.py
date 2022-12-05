##methods
ten_things = "Apple Oranges Crows Telephones Ravens Light Sugar"
print(ten_things.upper())
print(ten_things.lower())
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
print(stuff)
while len(stuff) != 10:
    ##take last item from more_stuff and add it to stuff
    next_one = more_stuff.pop()
    stuff.append(next_one)
    print("There are %s stuff" %(len(stuff)))
print(stuff)

##print last item
print(stuff[-1])

# print(stuff[3:5])

##join statemnents
# print(','.join(stuff))
print('################################################')

print('#'.join(stuff[3:5]))

##find method returns first index of character in find method
##if match is not found, returns -1
sentence = "Python course for beginners"
print(sentence.find("o"))

##replace method
sentence = sentence.replace("beginners", "experts")
print(sentence)

##use in to see if string exists
print('Python' in sentence)
