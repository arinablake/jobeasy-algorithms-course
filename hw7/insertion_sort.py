from random import randint
from operator import itemgetter


def insertion_sort(array, key='age'):
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while array[j] > key and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
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
print(f'insertion: {insertion_sort(a(key = lambda x: x['age']))}')


# N = 5
# a = []
# for i in range(N):
#     a.append(randint(1, 99))
#
# print(f'original: {a}')
# print('\n')
# print(f'insertion: {insertion_sort(a)}')

# N = 5

# key = lambda x: x['age']
# new_list = insertion_sort(a, key=itemgetter('age'))