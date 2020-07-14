# The museum of incredible dull things
# The museum of incredible dull things wants to get rid of some exhibitions. Miriam, the interior architect, comes up with a plan to remove the most boring exhibitions. She gives them a rating, and then removes the one with the lowest rating.
#
# However, just as she finished rating all exhibitions, she's off to an important fair, so she asks you to write a program that tells her the ratings of the items after one removed the lowest one. Fair enough.
#
# Task
# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.
#
# Don't change the order of the elements that are left.
#
# Examples
# remove_smallest([1,2,3,4,5]) = [2,3,4,5]
# remove_smallest([5,3,2,1,4]) = [5,3,2,4]
# remove_smallest([2,2,1,2,1]) = [2,2,2,1]


def remove_smallest(numbers):
    print(numbers)
    if len(numbers) < 1:
        return []
    else:
        new_list = numbers[:]
        min1 = numbers[0]
        index = 0
        while index < len(numbers):
            if numbers[index] < min1:
                min1 = numbers[index]
            index += 1
        new_list.remove(min1)
        return new_list


print(remove_smallest([1, 2, 1, -3, 3, 4, 5]))
