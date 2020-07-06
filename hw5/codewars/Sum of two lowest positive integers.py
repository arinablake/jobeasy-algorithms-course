# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
#
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
#
# [10, 343445353, 3453445, 3453545353453] should return 3453455.


def sum_two_smallest_numbers(numbers):
    min1 = numbers[0]
    index = 0
    while index < len(numbers):
        if numbers[index] < min1:
            min1 = numbers[index]
        index += 1
    numbers.remove(min1)
    min2 = numbers[0]
    index = 0
    while index < len(numbers):
        if numbers[index] < min2:
            min2 = numbers[index]
        index += 1
    return min1 + min2

print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))