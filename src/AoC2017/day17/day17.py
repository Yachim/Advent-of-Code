# insert after
def get_next_index(seq, index: int, step_cnt: int):
    return (index + step_cnt) % len(seq)

def part1(step_cnt: int):
    buffer = [0]
    current_index = 0
    for i in range(1, 2018):
        next_i = get_next_index(buffer, current_index, step_cnt)
        buffer.insert(next_i + 1, i)
        current_index = next_i + 1

    return buffer[current_index + 1]

def part2(step_cnt: int):
    buffer = [0]
    current_index = 0
    for i in range(1, 50000001):
        next_i = get_next_index(buffer, current_index, step_cnt)
        buffer.insert(next_i + 1, i)
        current_index = next_i + 1

    zero_index = buffer.index(0)
    return buffer[zero_index + 1]

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = int(f.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")