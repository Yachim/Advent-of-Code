input = [int(i) for i in open("input.txt", "r").read().splitlines()]

def part1():
    values = input.copy()
    output = []
    for i in range(len(values)):
        for j in range(1, len(values)):
            if values[i] + values[j] == 2020:
                output = [values[i], values[j]]
                break
        else: 
            continue
        break
    return (output[0]*output[1])

def part2():
    values = input.copy()
    output = []
    for i in range(len(values)):
        for j in range(1, len(values)):
            for l in range(2, len(values)):
                if values[i] + values[j] + values[l] == 2020:
                    output = [values[i], values[j], values[l]]
                    break
            else:
                continue
            break
        else: 
            continue
        break
    return (output[0]*output[1]*output[2])

print(part1())
print(part2())