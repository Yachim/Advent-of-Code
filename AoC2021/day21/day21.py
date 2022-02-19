from typing_extensions import TypeGuard


test = True

file_name = "input.txt" if not test else "testInput.txt"
input = open(file_name, "r").read().splitlines()
p1_pos = int(input[0][-1])
p2_pos = int(input[1][-1])

def part1():
    global p1_pos, p2_pos
    die = list(range(1,101))
    roll_count = 0
    index = 0
    p1 = 0
    p2 = 0
    while p1 < 1000 and p2 < 1000:
        p1_pos += (die[index%100] + die[(index+1)%100] + die[(index+2)%100])
        if p1_pos > 10:
            p1_pos %= 10
            if p1_pos == 0:
                p1_pos = 10
        index += 3
        p1 += p1_pos
        roll_count += 3
        if p1 >= 1000:
            return p2*roll_count

        p2_pos += (die[index%100] + die[(index+1)%100] + die[(index+2)%100])
        if p2_pos > 10:
            p2_pos %= 10
            if p2_pos == 0:
                p2_pos = 10
        index += 3
        p2 += p2_pos
        roll_count += 3
    return p1*roll_count

def eval_player(pos, score):
    if score >= 21:
        return 

def part2():
    pass

print(part1())
print(part2())