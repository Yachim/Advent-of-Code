from collections import Counter


def process_input(raw_in):
    return raw_in.splitlines()

def part1(inp):
    twice = 0
    thrice = 0

    for i in inp:
        cnt = Counter(i)

        if 2 in cnt.values(): twice += 1
        if 3 in cnt.values(): thrice += 1

    return twice * thrice

def part2(inp):
    for i, j in enumerate(inp):
        for k in inp[0:i] + inp[i + 1:]:
            wrong = 0
            wrong_index = []
            for l in range(len(j)):
                if j[l] != k[l]: 
                    wrong += 1
                    wrong_index = l

            if wrong == 1:
                return k[0:wrong_index] + k[wrong_index + 1:]
                

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = process_input(f.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")