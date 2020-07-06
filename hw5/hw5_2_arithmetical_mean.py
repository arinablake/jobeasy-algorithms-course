# When given a list, the program should return a list of all the elements that are below the arithmetical mean of the original list.
# The arithmetical mean is the sum of all elements divided by the number of elements.

from random import randint

length = int(input(f'Enter length of array '))
array = []

for i in range(length):
    item = randint(0, 100)
    array.append(item)
print(array)

summ = 0
arithm_mean = 0
for item in array:
    summ += item
arithm_mean = summ / len(array)
print(arithm_mean)

new_list = []
for item in array:
    if item < arithm_mean:
        new_list.append(item)
print(new_list)
