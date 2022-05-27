with open("input.txt", "r") as f:
    input = [i.split(" ") for i in f.read().splitlines()]

CONDITION_DICT = {
    ">": lambda x, y: x > y,
    "<": lambda x, y: x < y,
    ">=": lambda x, y: x >= y,
    "<=": lambda x, y: x <= y,
    "==": lambda x, y: x == y,
    "!=": lambda x, y: x != y,
}
COMM_DICT = {
    "inc": lambda x, y: x + y,
    "dec": lambda x, y: x - y
}

def solve(part2 = False):
    regs = {}
    highest = 0
    for i in input:
        reg = i[0]
        comm = i[1]
        num = int(i[2])
        reg_condition = i[4]
        condition = i[5]
        num_condition = int(i[6])

        if reg not in regs.keys():
            regs[reg] = 0
        if reg_condition not in regs.keys():
            regs[reg_condition] = 0

        if CONDITION_DICT[condition](regs[reg_condition], num_condition):
            regs[reg] = COMM_DICT[comm](regs[reg], num)
        
        highest = max([highest, regs[reg]])

    if part2:
        return highest
    return regs[max(regs, key=lambda x: regs[x])]


print(solve())
print(solve(True))