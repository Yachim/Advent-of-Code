
input = [i.split() for i in open("input.txt", "r").read().splitlines()]
IS = {"hlf": lambda x: x//2,
      "tpl": lambda x: 3*x,
      "inc": lambda x: x+1,
      "jio": lambda x, y: y if x==1 else 0,
      "jie": lambda x, y: y if x%2==0 else 0}

def part1():
    regs = {"a": 0, "b": 0}
    i = 0
    while True:
        if i >= len(input):
            return regs["b"]
        comm = input[i][0]
        if comm == "jio" or comm == "jie":
            reg = regs[input[i][1][0]]
            off = int(input[i][2])
            plus = IS[comm](reg, off)
        elif comm == "jmp":
            off = int(input[i][1])
            plus = off
        else:
            reg = int(regs[input[i][1]])
            regs[input[i][1]] = IS[comm](reg)
            plus = 1
        i += plus if plus != 0 else 1

def part2():
    regs = {"a": 1, "b": 0}
    i = 0
    while True:
        if i >= len(input):
            return regs["b"]
        comm = input[i][0]
        if comm == "jio" or comm == "jie":
            reg = regs[input[i][1][0]]
            off = int(input[i][2])
            plus = IS[comm](reg, off)
        elif comm == "jmp":
            off = int(input[i][1])
            plus = off
        else:
            reg = int(regs[input[i][1]])
            regs[input[i][1]] = IS[comm](reg)
            plus = 1
        i += plus if plus != 0 else 1

print(part1())
print(part2())