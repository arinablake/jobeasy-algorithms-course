# Write a Python function, which will count how many times a character (substring) is included in a string.
# # DON’T USE METHOD COUNT

x = str(input("Enter the symbol: "))
string = str(input("Enter the String: "))


def count_x(string):
    result = 0
    for i in string:
        if x == i:
            result += 1
    return result


print(count_x(string))
