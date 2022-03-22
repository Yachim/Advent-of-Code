input = open("input.txt","r").read().splitlines()

def part1():
    total = 0
    for i in input:
        i = [int(j) for j in i.split("x")]
        total += 2*(i[0]*i[1] + i[1]*i[2] + i[0]*i[2]) + min(i[0]*i[1], i[1]*i[2], i[0]*i[2])
    return total

def part2():
    total = 0
    for i in input:
        i = [int(j) for j in i.split("x")]
        per1 = 2*(i[0]+i[1])
        per2 = 2*(i[1]+i[2])
        per3 = 2*(i[0]+i[2])
        total += min(per1, per2, per3) + i[0]*i[1]*i[2]
    return total

print(part1())
print(part2())