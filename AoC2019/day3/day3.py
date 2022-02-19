#thanks for the help u/daggerdragon (https://www.reddit.com/r/adventofcode/comments/e5bz2w/2019_day_3_solutions/f9peu3o/?context=3)
input = [i.split(",") for i in open("input.txt", "r").read().splitlines()]

directions = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}

def part1():
    coords1 = [(0, 0)]
    coords2 = [(0, 0)]
    for i in input[0]:
        for j in range(int(i[1:])):
            new_x = coords1[-1][0]+(directions[i[0]][0])
            new_y = coords1[-1][1]+(directions[i[0]][1])
            new_coords = (new_x, new_y)
            coords1.append(new_coords)
    for i in input[1]:
        for j in range(int(i[1:])):
            new_x = coords2[-1][0]+(directions[i[0]][0])
            new_y = coords2[-1][1]+(directions[i[0]][1])
            new_coords = (new_x, new_y)
            coords2.append(new_coords)
    intersections = set(coords1) & set(coords2)
    intersections.remove((0,0))
    return min(abs(x)+abs(y) for (x, y) in intersections)

def part2():
    coords1 = [(0, 0)]
    coords2 = [(0, 0)]
    for i in input[0]:
        for j in range(int(i[1:])):
            new_x = coords1[-1][0]+(directions[i[0]][0])
            new_y = coords1[-1][1]+(directions[i[0]][1])
            new_coords = (new_x, new_y)
            coords1.append(new_coords)
    for i in input[1]:
        for j in range(int(i[1:])):
            new_x = coords2[-1][0]+(directions[i[0]][0])
            new_y = coords2[-1][1]+(directions[i[0]][1])
            new_coords = (new_x, new_y)
            coords2.append(new_coords)
    intersections = set(coords1) & set(coords2)
    intersections.remove((0,0))
    return min(sum(coord.index(intersect) for coord in [coords1, coords2]) for intersect in intersections)


print(part1())
print(part2())