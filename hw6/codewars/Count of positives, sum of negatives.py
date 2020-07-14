# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
#
# If the input array is empty or null, return an empty array.
#
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


def count_positives_sum_negatives(arr):
    if len(arr) < 1:
        return []
    else:
        pos = 0
        neg = 0
        new_list = []
        for i in arr:
            if i > 0:
                pos += 1
            elif i < 0:
                neg += i
        new_list.append(pos)
        new_list.append(neg)
        return new_list


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
