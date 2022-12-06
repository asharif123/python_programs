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
numbers = [35,2,4,12,-2,-3,456,44,50,10]
#pass index and what to add
numbers.insert(4,"240")
numbers.remove("240 ")
print(numbers)

#removes last item in list
numbers.pop()
##empties our list
# numbers.clear()

##returns index of first occurence of item
numbers.index(-3)

##count number of occurances
numbers.count(2)