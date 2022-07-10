from concurrent.futures import process
import re


RE_INP = re.compile(r"Generator ([A-z]+) starts with (\d+)", re.MULTILINE)

FACTORS = {"A": 16807, "B": 48271}
CRITERIAS = {"A": 4, "B": 8}

def process_input(raw_in: str):
    out = {}

    for i in re.finditer(RE_INP, raw_in):
        out[i.group(1)] = int(i.group(2))

    return out

def calculate_val(gen: str, val: int):
    return (val * FACTORS[gen]) % 2147483647

def matches(valA: int, valB: int):
    valA = bin(valA)[2:].zfill(16)
    valA = valA[len(valA) - 16:]

    valB = bin(valB)[2:].zfill(16)
    valB = valB[len(valB) - 16:]

    
    return valA == valB


def solve(inp: str, iters, part2=False):
    cnt = 0
    inp_obj = process_input(inp)

    if part2:
        a_vals = []
        b_vals = []

    i = 0
    while i < iters:
        inp_obj["A"] = calculate_val("A", inp_obj["A"])
        inp_obj["B"] = calculate_val("B", inp_obj["B"])

        if part2:
            if inp_obj["A"] % CRITERIAS["A"] != 0: a_vals.append(inp_obj["A"])
            if inp_obj["B"] % CRITERIAS["B"] != 0: b_vals.append(inp_obj["B"])

            if len(a_vals) != 0 and len(b_vals) != 0:
                if matches(a_vals.pop(0), b_vals.pop(0)): cnt += 1
                i += 1

            continue

        if matches(inp_obj["A"], inp_obj["B"]): cnt += 1
        i += 1
        
    return cnt


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = f.read()

    print(solve(inp, 40000000))
    print(solve(inp, 5000000, True))