# Recursion for Fib, factorial, digital root

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-2) + fib(n - 1)
print(fib(6))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))



def digital_root(n):
    result = 0
    for i in str(n):
        result += int(i)
    if len(str(result)) > 1:
        result = digital_root(result)
    return result

print(digital_root(n))