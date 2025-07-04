import math


def factorial(num):
    num_str = input('Enter the number :')
    num = int(num_str)
    if num < 2:
        return 1
    else:
        result = math.factorial(num)
        print(f"The factorial of {num} is: {result}")
        return None
factorial(5)


