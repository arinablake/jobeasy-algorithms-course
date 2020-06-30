# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
#
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"


def reverse_words(str):
    new_string = []
    for i in str.split(' '):
        new_string.append(i[::-1])
    return ' '.join(new_string)

print(reverse_words("This is an example!"))