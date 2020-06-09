# Count odd and even numbers.  Count odd and even digits of the whole number.
# E.g, if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).

n = int(input('Enter number '))


def count_odd_even(num):
    odd_count = 0
    even_count = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = num // 10
    print(f'There are {even_count} even digits in a number')
    print(f'There are {odd_count} odd digits in a number')


count_odd_even(n)
