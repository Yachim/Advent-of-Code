from math import sqrt


def part1(input):
    side = int(sqrt(input)) # size of the closest full side
    if side % 2 == 0:
        side -= 1

    root_rem = input - side*side
    dist_1 = int(side / 2)
    dist_2 = dist_1
    if root_rem == 0:
        return dist_1 + dist_2
    
    part_of_circle = side + 1 # size + one corner
    half_side = int(part_of_circle / 2)
    full_sides_cnt = int(root_rem / part_of_circle) # number of full sides
    center_num = side*side + full_sides_cnt * part_of_circle + half_side # number at the center of side

    dist_1 += 1
    dist_2 = abs(center_num - input)

    return dist_1 + dist_2

# brute force
def part2(input):
    numbers = [[(1, 1)]] # (index, val)
    coords = {"ix": 0, "iy": 0}
    coords["ix"] = 0
    coords["iy"] = 0
    side = 1
    cnt = 2

    while True:
        new_side = side + 2
        half_side = int(new_side / 2)
        coords["ix"] += 1
        coords["iy"] += 1      

        for i in range(len(numbers)):
            numbers[i] = [(float("inf"), 0)] + numbers[i] + [(float("inf"), 0)]
        numbers.insert(0, [(float("inf"), 0)] * new_side)
        numbers.append([(float("inf"), 0)] * new_side)
        side = new_side


        new_side = side + 2
        half_side = int(new_side / 2)
        coords["ix"] += 1
        coords["iy"] += 1  

        for i in range(len(numbers)):
            numbers[i] = [(float("inf"), 0)] + numbers[i] + [(float("inf"), 0)]
        numbers.insert(0, [(float("inf"), 0)]*new_side)
        numbers.append([(float("inf"), 0)]*new_side)
        side = new_side
        

        coords["ix"] += 1
        coords["iy"] += 1

        for i in [lambda x: coords[x] - 1, lambda x: coords[x] + 1]:
            for j in ["iy", "ix"]:
                for k in range(half_side):
                    coords[j] = i(j)
                    neighbours = [
                                numbers[coords["iy"]-1][coords["ix"]-1],
                                numbers[coords["iy"]-1][coords["ix"]],
                                numbers[coords["iy"]-1][coords["ix"]+1],
                                numbers[coords["iy"]][coords["ix"]-1],
                                numbers[coords["iy"]][coords["ix"]+1],
                                numbers[coords["iy"]+1][coords["ix"]-1],
                                numbers[coords["iy"]+1][coords["ix"]],
                                numbers[coords["iy"]+1][coords["ix"]+1]
                    ]
                    numbers[coords["iy"]][coords["ix"]] = (cnt, sum(l[1] for l in neighbours if l[0] < numbers[coords["iy"]][coords["ix"]][0]))
                    cnt += 1

                    if numbers[coords["iy"]][coords["ix"]][1] > input:
                        return numbers[coords["iy"]][coords["ix"]][1]


print(part1(1))
print(part1(12))
print(part1(23))
print(part1(1024))
with open("input.txt", "r") as f:
    input = int(f.read())
    print(part1(input))
    print(part2(input))