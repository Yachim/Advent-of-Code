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

def addr(bef, ins): 
    a = bef[ins[1]]
    b = bef[ins[2]]

    return a + b

def addi(bef, ins): 
    a = bef[ins[1]]
    b = ins[2]

    return a + b

def mulr(bef, ins): 
    a = bef[ins[1]]
    b = bef[ins[2]]

    return a * b

def muli(bef, ins): 
    a = bef[ins[1]]
    b = ins[2]

    return a * b 

def banr(bef, ins): 
    a = bef[ins[1]]
    b = bef[ins[2]]

    return a & b

def bani(bef, ins): 
    a = bef[ins[1]]
    b = ins[2]

    return a & b

def borr(bef, ins): 
    a = bef[ins[1]]
    b = bef[ins[2]]

    return a | b

def bori(bef, ins): 
    a = bef[ins[1]]
    b = ins[2]

    return a | b

def setr(bef, ins): 
    a = bef[ins[1]]

    return a

def seti(bef, ins): 
    a = ins[1]

    return a

def gtir(bef, ins): 
    a = ins[1]
    b = bef[ins[2]]

    if a > b: return 1
    return 0

def gtri(bef, ins): 
    a = bef[ins[1]]
    b = ins[2]

    if a > b: return 1
    return 0

def gtrr(bef, ins): 
    a = bef[ins[1]]
    b = bef[ins[2]]
    
    if a > b: return 1
    return 0

def eqir(bef, ins): 
    a = ins[1]
    b = bef[ins[2]]

    if a == b: return 1
    return 0

def eqri(bef, ins): 
    a = bef[ins[1]]
    b = ins[2]

    if a == b: return 1
    return 0

def eqrr(bef, ins): 
    a = bef[ins[1]]
    b = bef[ins[2]]

    if a == b: return 1
    return 0


functions = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr
}

def part1(inp):
    cnt = 0

    for sample in inp[0]:
        function_cnt = 0
        for function in functions.values():
            bef = sample["before"]
            ins = sample["instruction"]
            aft = sample["after"]
            if function(
                bef, 
                ins
            ) == aft[ins[3]]:  
                function_cnt += 1

            if function_cnt >= 3:
                cnt += 1
                break

    return cnt

def part2(inp):
    function_combinations = {}

    for sample in inp[0]:
        possible_functions = set()
        for function in functions:
            bef = sample["before"]
            ins = sample["instruction"]
            aft = sample["after"]
            if functions[function](
                bef, 
                ins
            ) == aft[ins[3]]:  
                possible_functions.add(function)
            
        if ins[0] not in function_combinations:
            function_combinations[ins[0]] = possible_functions.copy()
        else:
            new_functions = function_combinations[ins[0]].copy() & possible_functions.copy()
            function_combinations[ins[0]] = new_functions

    while not all([len(function_combinations[i]) == 1 for i in function_combinations]):
        one_function = list(filter(lambda x: len(function_combinations[x]) == 1, function_combinations))
        
        for function_to_remove in one_function:
            for function in function_combinations:
                if function == function_to_remove: continue
                
                function_to_remove_name = list(function_combinations[function_to_remove])[0]
                if function_to_remove_name in function_combinations[function]:
                    function_combinations[function].remove(function_to_remove_name)

    for function in function_combinations:
        function_name = list(function_combinations[function])[0]
        function_combinations[function] = function_name

    registers = [0, 0, 0, 0]
    for ins in inp[1]:
        op_code = function_combinations[ins[0]]
        registers[ins[3]] = functions[op_code](registers, ins)

    return registers[0]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = process_input(f.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")