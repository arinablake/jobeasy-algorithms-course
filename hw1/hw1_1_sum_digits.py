# Sum of 3 modified
# #  Homework: Rewrite a program with any number of digits.
# #  Instead of  3 digits, you should sum digits up from n digits number,
# #  Where  User enters n manually. n > 0

from random import randint

dig_num = int(input('Enter how many digits are in number '))


def sum_digits(digits):
    if digits < 1:
        print(digits)
    down = 10 ** (digits - 1)
    up = 10 ** digits - 1
    n = randint(down, up)
    print(n)
    result = 0
    i = 0
    while i < digits:
        result += n % 10
        n = n // 10
        i += 1
    return result


print(sum_digits(dig_num))
