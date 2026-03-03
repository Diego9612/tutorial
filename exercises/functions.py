#Function
#THe code inside the function is not executed
#until its called explicitly
def greeting():
    print("Hello, World!")

greeting ()
ret = greeting()

print(f"The function has implicitly returned {ret}")

# Type Hints: not actually enforced by the interpreter
# mypy
def greeting_name(name: str, surname: str, age: int) ->None:
# Union[list,dict]    
    print(f"Hello, my name is {name} {surname} and im {age} years old")
    return

# positional arguments: correct order is mandatory
greeting_name("Diego", "Huanca", 33)
# keyword arguments: can pass in any order
greeting_name(age = 33, name = "Diego", surname ="Huanca")
# mixed positional arguments first
greeting_name("Diego", age= 33, surname ="Huanca")

# optional argument food_2 with a default
def favourite_food(food_1, food_2 ="pizza"):

    return f"My favourite food is {food_1}, but i also like {food_2}"

output = favourite_food("chocolate")
print(output)
print(favourite_food("chocaolte", "sushi"))

def my_sum(*ejemplo):
    result = 0 
    for num in ejemplo:
        result += num
    return result
print(my_sum())
print(my_sum(3))
print(my_sum(3, 5 ,62 ,612))
print(my_sum(1_2424, 1_21412_12412, 2_213))
print(my_sum())

l = list(range(10))
print(my_sum(*l))


def test-function(regular_argument. *args, **kwargs):
print(regular_argument)
print(args)
print()
print()
print()