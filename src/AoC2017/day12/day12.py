import string


def process_input(raw_str: string) -> object:
    output = {}
    for i in raw_str.splitlines():
        [program, connected] = i.split(" <-> ")
        program = int(program)
        connected = set(int(j) for j in connected.split(", "))

        output[program] = connected

    return output

def part1(input: dict) -> int:
    searched = set()
    to_search = {0}
    while to_search:
        program = to_search.pop()
        for i in input[program]:
            if i not in searched:
                to_search.add(i)
        searched.add(program)

    return len(searched)

def part2(input: dict) -> int:
    input = input.copy()
    searched = set()
    groups = 0
    while input:
        to_search = {list(input.keys())[0]}
        while to_search:
            program = to_search.pop()
            for i in input[program]:
                if i not in searched and i != program:
                    to_search.add(i)
            searched.add(program)
            input.pop(program)
        
        groups += 1

    return groups

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = process_input(f.read())

    print(part1(input))
    print(part2(input))