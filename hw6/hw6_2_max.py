# Find the biggest number in the list (divide and rule)


# def find_max(lst, left, right):
#     if left == right:
#         return lst[left]
#     else:
#         mid = int((left + right) / 2)
#         max1 = find_max(lst, left, mid)
#         max2 = find_max(lst, mid + 1, right)
#         if max1 > max2:
#             return max1
#         else:
#             return max2
#
#
# lst = [2, 5, 4, 9, 3, 17, 5, 1, 10, 6]
# print('Maximum element of the list is', find_max(lst, 0, len(lst) - 1))


def biggest(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    mid = len(array) // 2
    max1 = biggest(array[:mid])
    max2 = biggest(array[mid:])
    if max1 > max2:
        return max1
    else:
        return max2


print('Maximum element of the list is', biggest([2, 5, 4, 11, 9, 3, 17, 5, 19, 10, 6]))