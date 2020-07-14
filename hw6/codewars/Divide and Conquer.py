# Given a mixed array of number and string representations of integers,
# add up the string integers and subtract this from the total of the non-string integers.
#
# Return as a number.


def div_con(x):
    integers = []
    strings = []
    for item in x:
        if type(item) == int:
            integers.append(item)
        else:
            strings.append(int(item))
    return sum(integers) - sum(strings)


print(div_con(['4', '0', 9, 3, 2, 1, '9', 6, 7]))