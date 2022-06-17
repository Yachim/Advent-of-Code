import re

input = open("input.txt", "r").read()

RE = r"([0-9])\1*"

def part1():
    inpt = input
    for i in range(40):
        string = ""
        for j in re.finditer(RE, inpt):
            match = j.group(0)
            string += str(len(match))+match[0]
        inpt = string
    return len(inpt)

def part2():
    inpt = input
    for i in range(50):
        string = ""
        for j in re.finditer(RE, inpt):
            match = j.group(0)
            string += str(len(match))+match[0]
        inpt = string
    return len(inpt)

print(part1())
print(part2())