# Enter a string of words separated by spaces. Find the longest word.

# 'iPhone 11 Pro lets you capture videos that are beautifully true to life, with greater detail and smoother motion.'


def long_word(string):
    array = string.split()
    longest_word = 0
    for i in range(1, len(array)):
        if len(array[longest_word]) < len(array[i]):
            longest_word = i
    return array[longest_word]


print(long_word('iPhone 11 Pro lets you capture videos that are beautifully true to life, with greater detail and smoother motion. '))
