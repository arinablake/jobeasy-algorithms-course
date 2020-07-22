from random import randint


def bubble(array):
    for item in range(len(array)):
        j = 0
        while j < len(array) - 1:
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j += 1
        print(array)
    return array


n = 5
a = []
for i in range(n):
    a.append(randint(1, 99))

print(f'original: {a}')
print('\n')
print(f'bubble: {bubble(a)}')

# def bubble(array):
#     for item in range(len(array)):
#         j = len(array) - 1
#         while j > 0:
#             if array[j] < array[j - 1]:
#                 array[j], array[j - 1] = array[j - 1], array[j]
#             j -= 1
#         print(array)
#     return array
