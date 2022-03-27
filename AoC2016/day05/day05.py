from hashlib import md5

input = open("input.txt", "r").read()

def part1():
    i = 0
    searches = 0
    p = ""
    while searches < 8:
        h = md5(str.encode(input + str(i))).hexdigest()
        if h[:5] == "00000":
            searches += 1
            p += h[5]
        i += 1
    return p    

def part2():
    i = 0
    p = [None] * 8
    while None in p:
        h = md5(str.encode(input + str(i))).hexdigest()
        if h[:5] == "00000":
            indx = h[5]
            if indx.isdigit() and int(indx) < len(p) and p[int(indx)] == None:
                p[int(indx)] = h[6]
        i += 1
    return "".join(p)    

print(part1())
print(part2())