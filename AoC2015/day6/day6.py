input = [i.split(" ") for i in open("input.txt", "r").read().splitlines()]

def part1():
    lights = [[False for i in range(1000)] for j in range(1000)]
    for i in input:
        if i[0] == "turn":
            i.pop(0)
        coords1 = [int(j) for j in i[1].split(",")]
        coords2 = [int(j) for j in i[3].split(",")]
        for j in range(min(coords1[1], coords2[1]), max(coords1[1], coords2[1])+1):
            for k in range(min(coords1[0], coords2[0]), max(coords1[0], coords2[0])+1):
                if i[0] == "toggle":
                    lights[j][k] = not lights[j][k]
                elif i[0] == "on":
                    lights[j][k] = True
                elif i[0] == "off":
                    lights[j][k] = False
    return sum([sum(i) for i in lights])

def part2():
    lights = [[0 for i in range(1000)] for j in range(1000)]
    for i in input:
        if i[0] == "turn":
            i.pop(0)
        coords1 = [int(j) for j in i[1].split(",")]
        coords2 = [int(j) for j in i[3].split(",")]
        for j in range(min(coords1[1], coords2[1]), max(coords1[1], coords2[1])+1):
            for k in range(min(coords1[0], coords2[0]), max(coords1[0], coords2[0])+1):
                if i[0] == "toggle":
                    lights[j][k] += 2
                elif i[0] == "on":
                    lights[j][k] += 1
                elif i[0] == "off" and lights[j][k] != 0:
                    lights[j][k] -= 1
    return sum([sum(i) for i in lights])

print(part1())
print(part2())