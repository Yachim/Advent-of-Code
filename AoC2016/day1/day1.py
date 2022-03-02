input = open("input.txt", "r").read().split(", ")

DIRS = ((1, 1), (0, 1), (1, -1), (0, -1)) # (up, right, down, left); (coord_index, multiplier - -1/1)
ROTS = {"R": 1, "L": -1} # index change in DIRS

def part1():
    dir = 0 # index in DIRS
    coords = [0, 0]
    for i in input:
        dir += ROTS[i[0]]
        if dir < 0:
            dir = 3
        elif dir > 3:
            dir = 0
        coord, mult = DIRS[dir]
        coords[coord] += int(i[1:]) * mult
    return sum(map(abs, coords))

def part2():
    dir = 0 # index in DIRS
    coords_list = [[0, 0]]
    for i in input:
        dir += ROTS[i[0]]
        if dir < 0:
            dir = 3
        elif dir > 3: 
            dir = 0
        coord, mult = DIRS[dir]
        for j in range(int(i[1:])):
            coords = coords_list[-1].copy()
            coords[coord] += mult
            if coords in coords_list:
                return sum(map(abs, coords))
            coords_list.append(coords)

print(part1())
print(part2())