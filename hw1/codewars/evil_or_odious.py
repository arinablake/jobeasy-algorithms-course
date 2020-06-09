# The number n is Evil if it has an even number of 1's in its binary representation.
# The first few Evil numbers: 3, 5, 6, 9, 10, 12, 15, 17, 18, 20
#
# The number n is Odious if it has an odd number of 1's in its binary representation.
# The first few Odious numbers: 1, 2, 4, 7, 8, 11, 13, 14, 16, 19
#
# You have to write a function that determine if a number is Evil of Odious, function should return "It's Evil!" in case of evil number and "It's Odious!" in case of odious number.


def evil(n):
    bin_n = bin(n)[2:]
    count1 = 0
    for i in bin_n:
        if i == str(1):
            count1 += 1
    if count1 % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"


# def evil(n):
#     bin_n = bin(n)[2:]
#     print(bin_n)
#     count1 = 0
#     for i in bin_n:
#         if i == str(1):
#             count1 += 1
#             print(count1)
#     if count1 % 2 == 0:
#         print("It's Evil!")
#     else:
#         print("It's Odious!")
#
# evil(2)