import re

input = open("input.txt", "r").read().splitlines()

def part1():
    RE1 = r"\w*[aeiou]\w*[aeiou]\w*[aeiou]\w*"
    RE2 = r"\w*(\w)\1+\w*"
    RE3 = r"^((?!ab)(?!cd)(?!pq)(?!xy).)*$"

    nice = 0
    for i in input:
        if re.match(RE1, i) and re.match(RE2, i) and re.match(RE3, i):
            nice += 1
    return nice

def part2():
    RE1 = r"\w*(\w)(\w)\w*\1\2\w*"
    RE2 = r"\w*(\w)\w{1}\1\w*"
    nice = 0
    for i in input:
        if re.match(RE1, i) and re.match(RE2, i):
            nice += 1
    return nice

print(part1())
print(part2())