input = [int(i) for i in open("input.txt", "r").read().split(",")]

def part1():
    values = input.copy()
    values[1], values[2] = [12, 2]
    for i in range(0, len(values), 4):
        if values[i] == 99:
            break
        elif values[i] == 1:
            a = values[values[i+1]]
            b = values[values[i+2]]
            values[values[i+3]] = a+b
        elif values[i] == 2:
            a = values[values[i+1]]
            b = values[values[i+2]]
            values[values[i+3]] = a*b
    return values[0]

def part2():
    values = input.copy()
    for x in range(100):
        for y in range(100):
            values[1] = x
            values[2] = y
            for i in range(0, len(values), 4):
                if values[i] == 99:
                    if values[0] == 19690720:
                        return (100*values[1])+values[2]
                    else:
                        values = input.copy()
                        break
                elif values[i] == 1:
                    a = values[values[i+1]]
                    b = values[values[i+2]]
                    values[values[i+3]] = a+b
                elif values[i] == 2:
                    a = values[values[i+1]]
                    b = values[values[i+2]]
                    values[values[i+3]] = a*b

print(part1())
print(part2())