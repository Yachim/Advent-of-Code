import re

input = open("input.txt", "r").read()

RE = r"\((\d+)x(\d+)\)"

def part1():
    res = ""
    inpt = input
    m = re.search(RE, inpt)
    while m:
        cnt = int(m.group(1))
        times = int(m.group(2))
        s = m.start()
        e = m.end()
        
        res += inpt[:s] + times * inpt[e:e+cnt]
        inpt = inpt[e+cnt:]
        m = re.search(RE, inpt)
    res += inpt
    return len(res)

cache = {}
def part2(inpt=input):
    if inpt in cache: 
        return cache[inpt]
    elif re.search(RE, inpt):
        m = re.search(RE, inpt)
        cnt = int(m.group(1))
        times = int(m.group(2))
        s = m.start()
        e = m.end()
        
        l = len(inpt[:s]) + times * part2(inpt[e:e+cnt]) + part2(inpt[e+cnt:])
        cache[inpt] = l
        return l
    else:
        return len(inpt)

print(part1())
print(part2())