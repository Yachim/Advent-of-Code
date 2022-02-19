input = open("input.txt", "r").read().splitlines()


def part1():
    return sum(len(i)-len(eval(i)) for i in input)

def part2():
    return sum((len(i.replace("\\", "\\\\").replace("\"", "\"\""))+2)-len(i) for i in input) 
    
print(part1())
print(part2())