with open("input.txt", "r") as f:
    input1 = {}
    input2 = {}
    for i in f:
        sides = i[:-1].split(" -> ")
        left = sides[0].split(" ")
        right = sides[1].split(", ")
        input1[left[0]] = (int(left[1][1:-1]), tuple(right))

        for j in right:
            input2[j] = left[0]

def part1():
    pass

print(part1())