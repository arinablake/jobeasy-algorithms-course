from random import randint
from operator import itemgetter, attrgetter

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        print(array)
    return array

a = [
    {
        'name': 'Ilya',
        'age': 26
    },
    {
        'name': 'John',
        'age': 35
    },
    {
        'name': 'Patrick',
        'age': 17
    }
]


print(f'original: {a}')
print()
print(f'selection sort: {selection_sort(a, key=attrgetter('age')}')


# n = 5
# a = []
# for i in range(n):
#     a.append(randint(1, 99))
#
# print(f'original: {a}')
# print()
# print(f'selection: {selection_sort(a)}')