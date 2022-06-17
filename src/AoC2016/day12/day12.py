import re

input = open("input.txt", "r").read().splitlines()

RE = r"(\w{3}) (\d+|\w{1})(?: (-*\d+|\w{1}))*"
RE_DEC = r"dec (\w{1})" # regex for increase, decrease, jump -2 pattern, for example:
#inc a
#dec d
#jnz d -2

def solve(part2=False):
    regs = {i:0 for i in ["a", "b", "c", "d"]}
    if part2:
        regs["c"] = 1
    index = 0
    while index < len(input): 
        m = re.search(RE, input[index])
        cmd = m.group(1)

        x = m.group(2)
        if x.isnumeric():
            x = int(x)
        
        if cmd == "cpy":
            y = m.group(3)
            if isinstance(x, str):
                x = regs[x]

            regs[y] = x
        elif cmd == "inc":
            m2 = re.search(RE_DEC, input[index + 1])
            if m2: # optimization (see comment on line 6)
                reg = m2.group(1)
                if input[index + 2] == f"jnz {reg} -2":
                    regs[x] += regs[reg]
                    regs[reg] = 0
                    index += 2
            else:
                regs[x] += 1
        elif cmd == "dec":
            regs[x] -= 1
        elif cmd == "jnz":
            y = int(m.group(3))
            if isinstance(x, str):
                x = regs[x]

            if x != 0:
                index += y
                continue

        index += 1

    return regs["a"]

print(solve())
print(solve(True))