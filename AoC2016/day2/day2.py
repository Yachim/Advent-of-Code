input = open("input.txt", "r").read().splitlines()

DIRS = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}

def part1():
    KEYPAD = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 9))
    coords = [1, 1]
    code = ""
    for i in input:
        for j in i:
            old_coords = coords.copy()
            coords[0] += DIRS[j][0]
            coords[1] += DIRS[j][1]
            if coords[0] == -1 or coords[0] == 3 or coords[1] == -1 or coords[1] == 3:
                coords = old_coords
        code += str(KEYPAD[coords[1]][coords[0]])
    return code

def part2():
    KEYPAD =    ((None, None, "1", None, None),
                  (None, "2", "3", "4", None),
                   ("5", "6", "7", "8", "9"),
                  (None, "A", "B", "C", None),
                 (None, None, "D", None, None))
    coords = [2, 0]
    code = "" 
    for i in input:
        for j in i:
            old_coords = coords.copy()
            coords[0] += DIRS[j][0]
            coords[1] += DIRS[j][1]
            if coords[0] == -1 or coords[1] == -1 or coords[0] == 5 or coords[1] == 5 or KEYPAD[coords[1]][coords[0]] == None:
                coords = old_coords
        code += KEYPAD[coords[1]][coords[0]]
    return code

print(part1())
print(part2())