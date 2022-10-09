def process_input(raw_in: str):
    samples, tests = raw_in.split("\n\n\n\n")
    out = [[], []]

    samples = samples.split("\n\n")
    for sample in samples:
        bef, ins, aft = sample.splitlines()
        bef = bef[9:-1].split(", ")
        ins = ins.split(" ")
        aft = aft[9:-1].split(", ")

        out[0].append({
            "before": [int(i) for i in bef],
            "instruction": [int(i) for i in ins],
            "after": [int(i) for i in aft]
        })

    tests = tests.splitlines()
    for test in tests:
        test = test.split(" ")
        out[1].append([int(i) for i in test])

    return out

def is_addr(bef, ins, aft): 
    a = bef[ins[1]]
    b = bef[ins[2]]
    c = aft[ins[3]]

    return a + b == c

def is_addi(bef, ins, aft): 
    a = bef[ins[1]]
    b = ins[2]
    c = aft[ins[3]]

    return a + b == c

def is_mulr(bef, ins, aft): 
    a = bef[ins[1]]
    b = bef[ins[2]]
    c = aft[ins[3]]

    return a * b == c

def is_muli(bef, ins, aft): 
    a = bef[ins[1]]
    b = ins[2]
    c = aft[ins[3]]

    return a * b == c

def is_banr(bef, ins, aft): 
    a = bef[ins[1]]
    b = bef[ins[2]]
    c = aft[ins[3]]

    return a & b == c

def is_bani(bef, ins, aft): 
    a = bef[ins[1]]
    b = ins[2]
    c = aft[ins[3]]

    return a & b == c

def is_borr(bef, ins, aft): 
    a = bef[ins[1]]
    b = bef[ins[2]]
    c = aft[ins[3]]

    return a | b == c

def is_bori(bef, ins, aft): 
    a = bef[ins[1]]
    b = ins[2]
    c = aft[ins[3]]

    return a | b == c

def is_setr(bef, ins, aft): 
    a = bef[ins[1]]
    c = aft[ins[3]]

    return a == c

def is_seti(bef, ins, aft): 
    a = ins[1]
    c = aft[ins[3]]

    return a == c

def is_gtir(bef, ins, aft): 
    a = ins[1]
    b = bef[ins[2]]
    c = aft[ins[3]]

    return (a > b and c == 1) or c == 0

def is_gtri(bef, ins, aft): 
    a = bef[ins[1]]
    b = ins[2]
    c = aft[ins[3]]

    return (a > b and c == 1) or c == 0

def is_gtrr(bef, ins, aft): 
    a = bef[ins[1]]
    b = bef[ins[2]]
    c = aft[ins[3]]

    return (a > b and c == 1) or c == 0

def is_eqir(bef, ins, aft): 
    a = ins[1]
    b = bef[ins[2]]
    c = aft[ins[3]]

    return (a == b and c == 1) or c == 0

def is_eqri(bef, ins, aft): 
    a = bef[ins[1]]
    b = ins[2]
    c = aft[ins[3]]

    return (a == b and c == 1) or c == 0

def is_eqrr(bef, ins, aft): 
    a = bef[ins[1]]
    b = bef[ins[2]]
    c = aft[ins[3]]

    return (a == b and c == 1) or c == 0


functions = [
    is_addr,
    is_addi,
    is_mulr,
    is_muli,
    is_addr,
    is_addi,
    is_banr,
    is_bani,
    is_borr,
    is_bori,
    is_setr,
    is_seti,
    is_gtir,
    is_gtri,
    is_gtrr,
    is_eqir,
    is_eqri,
    is_eqrr
]

def part1(inp):
    cnt = 0

    for instruction in inp[0]:
        function_cnt = 0
        for function in functions:
            if function(instruction["before"], instruction["instruction"], instruction["after"]): 
                function_cnt += 1

            if function_cnt >= 3:
                cnt += 1
                break

    return cnt

def part2(inp):
    pass

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = process_input(f.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")