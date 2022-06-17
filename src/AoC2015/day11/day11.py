import re

input = open("input.txt", "r").read()

RE = r"^\w*(\w)\1+\w*(\w)\2+\w*$"

def increment(string):
    if string[-1] == "z":
        return increment(string[:-1])+"a"
    else:
        return string[:-1]+chr(ord(string[-1])+1)

def part1():
    inpt = input
    while True:
        while ("i" in inpt or "l" in inpt or "o" in inpt) or not re.match(RE, inpt):
            inpt = increment(inpt)
        match = re.match(RE, inpt)
        if match.group(1) == match.group(2):
            inpt = increment(inpt)
        for i in range(len(inpt)-3):
            if ord(inpt[i])+1 == ord(inpt[i+1])  == ord(inpt[i+2])-1:
                return inpt
        inpt = increment(inpt)

input = part1()
print(input)
input = increment(input)
print(part1())