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

# ##unpacking
# coordinates = (1,2,3)
# #unpacking coordinates tuple to 3 variables
# x,y,z = coordinates

##find second max in array
data = [55,1,88,159,35,159,1]
##keep track of first and second max
def find_second_maximum(list1):
    ##keep track of first and second max
    ##first max is max of first 2 elements
    ##then compare 3rd elements to end of list
    first_max =  max(list1[0], list1[1])
    second_max = min(list1[0], list1[1])
    for i in range(2,len(list1)):
    ##if number is bigger than first_max, update first_max to new value and second_max to original first_max
        if (list1[i] > first_max):
            second_max = first_max
            first_max = list1[i]
    ##if number is less than first max but bigger than old second_max, update second_max to new value
        elif (list1[i] < first_max and list1[i] > second_max):
            second_max = list1[i]
    return second_max
print(find_second_maximum(data))

##find second min in array
def find_second_min(list1):
    first_min = min(list1[0],list1[1])
    second_min = max(list1[0], list1[1])
    for i in range(2, len(list1)):
        if (first_min > list1[i]):
            second_min = first_min
            first_min = list1[i]
        elif (first_min < list1[i] and second_min > list1[i]):
            second_min = list1[i]
    return second_min
print(find_second_min(data))