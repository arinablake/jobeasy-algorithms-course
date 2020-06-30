# Enter an irregular string
# (that means it may have space at the beginning of a string, at the end of the string,
# and words may be separated by several spaces).
# Make the string regular (delete all spaces at the beginning and end of the string, leave one space separating words).

# '   Enter   an                       irregular      string   '


def clean_string(string):
    clean_beg_end = string.strip(' ')
    array = clean_beg_end.split(' ')
    result = []
    for item in array:
        if not item == '':
            result.append(item)
    return ' '.join(result)


print(clean_string('   Enter   an                       irregular      string   '))
