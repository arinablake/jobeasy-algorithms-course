array = [
    {
        'name': 'Ilya',
        'age': 26
    },
    {
        'name': 'John',
        'age': 35
    },
    {
        'name': 'Patrick',
        'age': 17
    }
]
array.sort(key=lambda k: k['age'])

print(array)


