# When given a list of elements find the two lowest elements.
# They can be equal to each other or different.


from random import randint

length = int(input(f'Enter length of array '))
array = []

for i in range(length):
    item = randint(0, 100)
    array.append(item)
print(array)

min1 = array[0]
index = 0
while index < len(array):
    if array[index] < min1:
        min1 = array[index]
    index += 1
# print(min1)

array.remove(min1)
# print(array)

min2 = array[0]
index = 0
while index < len(array):
    if array[index] < min2:
        min2 = array[index]
    index += 1
# print(min2)
print(min1, min2)

