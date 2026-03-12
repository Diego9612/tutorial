# function DEFinition
# The code inside the function is not executed
# until it's called explicitly
def greeting():
    print("Hello, World!")

greeting()
ret = greeting()
print(f"The function has implicitly returned {ret}")

# Type Hints: not actually enforced by the interpreter
def greeting_name(name: str, surname: str, age: int) -> None:
    print(f"Hello, my name is {name} {surname} and I'm {age} years old")
    return

# positional arguments: correct order is mandatory
greeting_name("Melody", "Uffre", 33)
# keyword arguments: can pass in any order
greeting_name(age=33, name="Melody", surname="Uffre")
# mixed: positional arguments first
greeting_name("Melody", age=33, surname="Uffre")

# optional argument food_2 with a default
def favourite_food(food_1, food_2="pizza"):
    return f"My favourite food is {food_1}, but I also like {food_2}"

output = favourite_food("chocolate")
print(output)
print(favourite_food("chocolate", "sushi"))

def my_sum(*args):
    result = 0
    for num in args:
        result += num
    return result

print(my_sum())
print(my_sum(3))
print(my_sum(3, 5, 19, 42))
print(my_sum(1_234, 1_000_000, 9_999))

# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l = list(range(10))
# print(my_sum(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
print(my_sum(*l))

def test_function(regular_argument, *args, **kwargs):
    print(regular_argument)
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

print("-" * 20)
test_function(1)
print("-" * 20)
test_function(1, 2, 3)
print("-" * 20)
test_function(1, 100, 200, cat="meow", dog="woof")
print("-" * 20)
test_function(regular_argument=1, cat="meow", dog="woof")