import math
from __pycache__.utils import get_int_input


def ex1():
    num1 = get_int_input("Write the first number: ")
    num2 = get_int_input("Write the second number: ")

    result = math.sqrt(num1 + num2)

    print("The square root of the sum is:", result)


def ex2():
    print("Please provide 3 integers separated by comma")

    values = input("Numbers: ")
    numbers = values.split(",")

    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])

    print("Sum:", a + b + c)

if __name__ == "__main__":
    ex1()   # o cambia a ex2()