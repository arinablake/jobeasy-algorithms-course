# Rewrite code, which will return only needed element of Fib sequence

num = int(input("Enter the Number: "))

first = 0
second = 1

for i in range(1, num + 1):
    if i <= 1:
        fib = i
    else:
        fib = first + second
        first = second
        second = fib

print(fib)


