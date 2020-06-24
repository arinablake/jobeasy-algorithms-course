# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
# Return the resulting string.


def fake_bin(x):
    string = ''
    for i in x:
        if int(i) < 5:
            string += '0'
        else:
            string += '1'
    return string


print(fake_bin('45385593107843568'))
