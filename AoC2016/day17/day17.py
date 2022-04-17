from hashlib import md5

with open("input.txt", "r") as f:
    input = f.read()

OPEN = ["b", "c", "d", "e", "f"]


def get_dist(coords): # taxicab distance used as heuristic
    x = 3 - coords[0]
    y = 3 - coords[1]
    return x + y

def part1():
    paths = {"": (0, 0)}

    while paths:
        path = min(paths, key=lambda x: len(x) + get_dist(paths[x])) 
        coords = paths.pop(path)
        h = md5(str.encode(input + path)).hexdigest()[:4]

        if coords == (3, 3):
            return path

        for i, j in enumerate(h):
            if j not in OPEN:
                continue
            if i == 0: # up
                if coords[1] == 0: # beyond border
                    continue
                new_coords = (coords[0], coords[1] - 1)
                new_path = path + "U"
            elif i == 1: # down
                if coords[1] == 3: # beyond border 
                    continue
                new_coords = (coords[0], coords[1] + 1)
                new_path = path + "D"
            elif i == 2: # left
                if coords[0] == 0: # beyond border
                    continue
                new_coords = (coords[0] - 1, coords[1])
                new_path = path + "L"
            elif i == 3: # right
                if coords[0] == 3: # beyond border
                    continue
                new_coords = (coords[0] + 1, coords[1])
                new_path = path + "R"

            if new_path not in paths.keys() or get_dist(paths[new_path]) > get_dist(new_coords):
                paths[new_path] = new_coords

    return

def part2(path="", coords=(0,0)):
    if coords == (3, 3):
        yield len(path)
        return

    h = md5(str.encode(input + path)).hexdigest()[:4]
    for i, j in enumerate(h):
        if j not in OPEN:
            continue
        if i == 0: # up
            if coords[1] == 0: # beyond border
                continue
            new_coords = (coords[0], coords[1] - 1)
            new_path = path + "U"
        elif i == 1: # down
            if coords[1] == 3: # beyond border 
                continue
            new_coords = (coords[0], coords[1] + 1)
            new_path = path + "D"
        elif i == 2: # left
            if coords[0] == 0: # beyond border
                continue
            new_coords = (coords[0] - 1, coords[1])
            new_path = path + "L"
        elif i == 3: # right
            if coords[0] == 3: # beyond border
                continue
            new_coords = (coords[0] + 1, coords[1])
            new_path = path + "R"

        yield from part2(new_path, new_coords)


    return

print(part1())
print(max(part2()))