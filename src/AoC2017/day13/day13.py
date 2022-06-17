from typing import Dict, Tuple


def process_input(raw_str: str) -> Dict[int, Tuple[int, int]]:
    out = {}
    for i in raw_str.splitlines():
        [key, val] = i.split(": ")
        out[int(key)] = int(val)

    return out

def get_current_index(iteration, length):
    if iteration < length:
        return iteration

    if int(iteration / (length - 1)) % 2 == 1:
        return length - iteration % (length - 1) - 1
    return iteration % (length - 1)

def part1(input: Dict[int, int]) -> int:
    severity = 0
    for i in input:
        depth = input[i]
        if get_current_index(i, depth) == 0:
            severity += depth * i

    return severity

def part1_one_line(input: Dict[int, int]) -> int:
    return sum(i*input[i] for i in input if get_current_index(i, input[i]) == 0)

def part2(input: Dict[int, int]) -> int:
    delay = 0
    while any(get_current_index(i + delay, input[i]) == 0 for i in input): # todo: nesmí být na 0. indexu 
        delay += 1
    
    return delay

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = process_input(f.read())
    print(part1(input))
    print(part2(input))