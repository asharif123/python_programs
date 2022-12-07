##lists
##find largest number in a list
numbers = [35,2,4,12,-2,-3,456,44,50,10]
max_value = numbers[0]
for i in range(1,len(numbers)):
    if (max_value < numbers[i]):
        max_value = numbers[i]
print(max_value)

##2D lists
matrix = [[1,2,3],[4,5,6],[7,8,9]]

#7
print(matrix[2][0])

##list methods
numbers = [35,2,4,12,-2,-3,456,44,50,10,2,2,22,18]
#pass index and what to add
numbers.insert(4,"240")
print(numbers)
numbers.remove("240")
print(numbers)

#removes last item in list
numbers.pop()
##empties our list
# numbers.clear()

##returns index of first occurence of item
numbers.index(-3)

##count number of occurances
# print(numbers.count(2))

#sort
# print(numbers.sort())

#reverse:
# print(numbers.reverse())

#copy
numbers2 = numbers.copy()
# print(numbers2)

#append
# numbers.append('append')
# print(numbers)
print(numbers)
##remove duplicates in a list
unique = []
for value in numbers:
    if value not in unique:
        unique.append(value)
print(unique)

##tuples: immutable (cannot change them)
#can only use count and index to get info
numbers = (1,2,3)

##unpacking
coordinates = (1,2,3)
#unpacking coordinates tuple to 3 variables
x,y,z = coordinates