from string import ascii_letters
#User a list comprehension to create a list
# of numers: the cubes of the numbers from 0 to 9 


cubed_list = [n** 3 for n in range (10)]
    
print(cubed_list)

nums = [0,1,2,3]
dobles = [n*2 for n in nums]

#start from a string: create a set 
#of the unique letters of the string
# in uppercase
text= "ammaccabanane"
upper_letter_set = set()
for let in text: 
    upper_letter_set.add(let.upper())

print(upper_letter_set)

# ord() returns the unicode point of a single letter
# ord("A") -> 65
# Use a dict comprehension to associate
# the unicode point to its letter
# for every letter in ascii_letters   
# el profe habla de hacero de forma tradicional y el otro creo que se refiere a usar comprehension
unicode_dict = {letter: ord(letter) for letter in ascii_letters}
print(unicode_dict)
from string import ascii_letters
{"A": 65, "B": 66, "C": 67, "D": 68}


# Generate a list of tuples:
# #The numbers from 0 to 9 and
# the string "even" or "odd"
# [(0, "even"), (q,"odd"), (2, "even"), (3,"odd"), ....]

num_list = []
for n in range (10):
    if n % 2 == 0:
        num_list.append((n, "even"))
    else:
        num_list.append((n, "odd"))

t = (n, "even") if n % 2 == 0 else (n, "odd")
num_list.append(t)

# list comprehension of the squares
# of all the even numbers up to 9
even_list = [n **2 for n in range (10) if n % 2 == 0]
print(even_list)

d = {
    3: "Fizz",
    5: "Buzz",
    7: "Fuzz",
    9: "Bizz",
}

for i in range(1,101):
    output = ""
    for num in d:
        if i % num == 0:
            output += d[num]

    if output == "":
        output = i
    
    print(output)