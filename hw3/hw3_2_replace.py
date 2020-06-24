# Find and replace a substring in a string for another substring.
# User enter from a keyboard a string and both substrings. DON’T USE METHOD REPLACE


tb_repl = str(input("Enter the str to be replaced: "))
repl = str(input("Enter the replacement: "))
string = str(input("Enter the String: "))

if len(tb_repl) == 1:
    string = list(string)
    result = []
    for i in string:
        if i == tb_repl:
            i = repl
            result.append(i)
        else:
            result.append(i)
    print(''.join(result))

elif len(tb_repl) > 1:
    string = string.split(' ')
    result = []
    for i in string:
        if i == tb_repl:
            i = repl
            result.append(i)
        else:
            result.append(i)
    print(' '.join(result))

