input = open("input.txt", "r").read().splitlines()

def part1():
    vals = input.copy()
    outs = [] # outputs
    for i in range(len(vals)):
        pos = [[0, 127],[0, 7]]
        val = 64 # value to substract
        for j in range(7):
            if vals[i][j] == "F":
                pos[0][1] -= val
            elif vals[i][j] == "B":
                pos[0][0] += val
            val/=2
        val = 4 # value to substract
        for j in range(3):
            if vals[i][j+7] == "L":
                pos[1][1] -= val
            elif vals[i][j+7] == "R":
                pos[1][0] += val
            val/=2
        outs.append((pos[0][0]*8)+pos[1][0])
    return max(outs)

def part2():
    vals = input.copy()
    outs = [] # outputs
    for i in range(len(vals)):
        pos = [[0, 127],[0, 7]]
        val = 64 # value to substract
        for j in range(7):
            if vals[i][j] == "F":
                pos[0][1] -= val
            elif vals[i][j] == "B":
                pos[0][0] += val
            val/=2
        val = 4 # value to substract
        for j in range(3):
            if vals[i][j+7] == "L":
                pos[1][1] -= val
            elif vals[i][j+7] == "R":
                pos[1][0] += val
            val/=2
        outs.append((pos[0][0]*8)+pos[1][0])
    outs.sort()
    for i in range(1, len(outs)-1):
        if outs[i-1] == outs[i] - 2:
            return outs[i]-1


print(part1())
print(part2())