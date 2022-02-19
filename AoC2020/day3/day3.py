temp_input = open("input.txt", "r").read().splitlines()
input = []
for i in temp_input:
    temp_arr = []
    for j in i:
        temp_arr.append(j)
    input.append(temp_arr)
del temp_arr, temp_input

def part1():
    tree_count = 0
    x_index = 0
    y_index = 0
    while y_index < len(input)-1:
        x_index += 3
        y_index += 1
        if x_index >= len(input[y_index]):
            x_index-=len(input[y_index])
        if input[y_index][x_index] == "#":
            tree_count += 1
    return tree_count

def part2():
    tree_count1 = 0
    tree_count2 = 0
    tree_count3 = 0
    tree_count4 = 0
    tree_count5 = 0

    x_index = 0
    y_index = 0
    while y_index < len(input)-1:
        x_index += 1
        y_index += 1
        if x_index >= len(input[y_index]):
            x_index-=len(input[y_index])
        if input[y_index][x_index] == "#":
            tree_count1 += 1

    x_index = 0
    y_index = 0
    while y_index < len(input)-1:
        x_index += 3
        y_index += 1
        if x_index >= len(input[y_index]):
            x_index-=len(input[y_index])
        if input[y_index][x_index] == "#":
            tree_count2 += 1

    x_index = 0
    y_index = 0
    while y_index < len(input)-1:
        x_index += 5
        y_index += 1
        if x_index >= len(input[y_index]):
            x_index-=len(input[y_index])
        if input[y_index][x_index] == "#":
            tree_count3 += 1

    x_index = 0
    y_index = 0
    while y_index < len(input)-1:
        x_index += 7
        y_index += 1
        if x_index >= len(input[y_index]):
            x_index-=len(input[y_index])
        if input[y_index][x_index] == "#":
            tree_count4 += 1

    x_index = 0
    y_index = 0
    while y_index < len(input)-2:
        x_index += 1
        y_index += 2
        if x_index >= len(input[y_index]):
            x_index-=len(input[y_index])
        if input[y_index][x_index] == "#":
            tree_count5 += 1

    return tree_count1*tree_count2*tree_count3*tree_count4*tree_count5


print(part1())
print(part2())