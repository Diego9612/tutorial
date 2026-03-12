d = {
    3: "Fizz",
    5: "Buzz",
    7: "Fuzz",
    11: "Bizz",
}

for i in range(1, 101):
    output = ""
    for num in d:
        if i % num == 0:
            output += d[num]
    
    if output == "":
        output = i
    print(output)