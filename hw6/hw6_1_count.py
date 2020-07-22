# Write a recursive function to count all the elements in a list (divide and rule).

# 1)count how many elements are in the array


def array(lst):
    if lst == []:
        return 0
    else:
        return 1 + array(lst[1:])

print(array([1, 2, 2, 2, 2, 3, 4, 7, 8, 8]))


# 2)count how many times each element occurs in the array


# def count(f, s):
#     if s == []:
#         return 0
#     elif f == s[0]:
#         return 1 + count(f, s[1:])
#     else:
#         return 0 + count(f, s[1:])
#
#
# print(count(2, [1, 2, 2, 2, 2, 3, 4, 7, 4, 8, 8]))
