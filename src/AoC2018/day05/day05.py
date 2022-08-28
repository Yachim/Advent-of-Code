import re


# two same letters
RE1 = re.compile(r"([a-z])\1", re.IGNORECASE)
# alternating case
RE2 = re.compile(r"[a-z][A-Z]|[A-Z][a-z]")

def part1(inp: str):
    units = len(inp)

    inp_ = inp
    while RE1.search(inp):
        for i in RE1.finditer(inp_):
            if RE2.match(i.group(0)):
                ind = i.regs[0][0]

                units -= 2
                bef = inp[:ind]
                aft = inp[ind + 2:]
                inp = bef + aft

        inp_ = inp

    return units


def part2(inp):
    pass

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = f.read()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")