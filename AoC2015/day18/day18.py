from copy import deepcopy

def handle_input(line):
    new_line = [False]
    for i in line:
        new_line.append(True if i == "#" else False)
    return new_line + [False]

input = [[False]*102] + list(map(handle_input, open("input.txt", "r").read().splitlines())) + [[False]*102]

def part1(): 
    inpt2 = deepcopy(input)
    for m in range(100):
        inpt = deepcopy(inpt2)
        for i, j in enumerate(inpt[1:len(inpt)-1], 1):
            for k, l in enumerate(j[1:len(inpt)-1], 1):
                neighbours = [inpt[i-1][k-1], inpt[i-1][k], inpt[i-1][k+1], inpt[i][k-1], inpt[i][k+1], inpt[i+1][k-1], inpt[i+1][k], inpt[i+1][k+1]]
                if l and (neighbours.count(True) != 2 and neighbours.count(True) != 3):
                    inpt2[i][k] = False 
                elif not l and neighbours.count(True) == 3:
                    inpt2[i][k] = True
    return sum(map(lambda x: x.count(True), inpt2))

def part2(): 
    inpt2 = deepcopy(input)
    inpt2[1][1] = True
    inpt2[1][len(inpt2)-2] = True
    inpt2[len(inpt2)-2][1] = True
    inpt2[len(inpt2)-2][len(inpt2)-2] = True
    for m in range(100):
        inpt = deepcopy(inpt2)
        for i, j in enumerate(inpt[1:len(inpt)-1], 1):
            for k, l in enumerate(j[1:len(inpt)-1], 1):
                neighbours = [inpt[i-1][k-1], inpt[i-1][k], inpt[i-1][k+1], inpt[i][k-1], inpt[i][k+1], inpt[i+1][k-1], inpt[i+1][k], inpt[i+1][k+1]]
                if l and (neighbours.count(True) != 2 and neighbours.count(True) != 3):
                    inpt2[i][k] = False 
                elif not l and neighbours.count(True) == 3:
                    inpt2[i][k] = True
        inpt2[1][1] = True
        inpt2[1][len(inpt2)-2] = True
        inpt2[len(inpt2)-2][1] = True
        inpt2[len(inpt2)-2][len(inpt2)-2] = True
    return sum(map(lambda x: x.count(True), inpt2))

print(part1())
print(part2())