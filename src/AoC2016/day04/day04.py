import re
from collections import Counter

input = open("input.txt", "r").read().splitlines()

RE = r"^([a-zA-Z-]+)(\d+)\[(\w{5})\]$"

def part1():
    s = 0
    for i in input:
        m = re.match(RE, i)
        if m:
            letters = m.group(1).replace("-", "")
            c = list(Counter(letters).items())
            c.sort(key=lambda x: x[0])
            c.sort(key=lambda x: x[1], reverse=True)
            c = c[:5]
            
            checksum = "".join(j[0] for j in c)
            if checksum == m.group(3):
                s += int(m.group(2))
    return s

def decode(string, shift):
    new_str = ""
    for i in string:
        if i == "-":
            new_str += " "
        else:
            u = (ord(i) - 97 + shift) % 26 + 97
            new_str += chr(u)
    return new_str

def part2():
    for i in input:
        m = re.match(RE, i)
        if m:
            letters = m.group(1).replace("-", "")
            c = list(Counter(letters).items())
            c.sort(key=lambda x: x[0])
            c.sort(key=lambda x: x[1], reverse=True)
            c = c[:5]
            
            checksum = "".join(j[0] for j in c)
            if checksum == m.group(3):
                if "north" in decode(m.group(1), int(m.group(2))):
                    return m.group(2)

print(part1())
print(part2())