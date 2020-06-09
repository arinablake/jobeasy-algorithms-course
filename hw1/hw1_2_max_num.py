# Find max number from 3 values, entered manually from a keyboard

num1 = int(input('Enter 1st number '))
num2 = int(input('Enter 2nd number '))
num3 = int(input('Enter 3rd number '))


def max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f'Max number is 1st number {num1}')
    elif num2 > num1 and num2 > num3:
        print(f'Max number is 2nd number {num2}')
    elif num1 == num2:
        print(f'1st number {num1} is equal to 2nd number {num2}')
    elif num2 == num3:
        print(f'2nd number {num2} is equal to 3rd number {num3}')
    elif num1 == num3:
        print(f'1st number {num1} is equal to 3rd number {num3}')
    else:
        print(f'Max number is 3rd number {num3}')


max_number(num1, num2, num3)
