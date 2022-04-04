from math import sqrt

input = int(open("input.txt").read())

def is_wall(x, y):
    num = x*x + 3*x + 2*x*y + y + y*y
    num += input
    cnt = bin(num).count("1")

    return False if cnt % 2 == 0 else True

def calculate_dist(x, y, target_x, target_y):
    x_len = target_x - x
    y_len = target_y - y

    return sqrt(x_len ** 2 + y_len ** 2)

def part1():
    target_x = 31
    target_y = 39
    paths = {(1, 1):0} 
    closed_paths = set()
    
    while paths:
        path = min(paths, key = lambda x: paths[x] + calculate_dist(*x, target_x, target_y))
        steps = paths.pop(path)
        if path in closed_paths:
            continue
        if path[0] == target_x and path[1] == target_y:
            return steps

        for i in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            new_path = (path[0] + i[0], path[1] + i[1])
            if not is_wall(*new_path) and (new_path not in paths.keys() or paths[new_path] > steps + 1):
                paths[new_path] = steps + 1
        closed_paths.add(path)

def part2():
    paths = {(1, 1):0} 
    closed_paths = set()
    
    while paths:
        path = list(paths.keys())[0]
        steps = paths.pop(path)
        if path in closed_paths or steps > 50:
            continue

        for i in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            new_path = (path[0] + i[0], path[1] + i[1])
            if not is_wall(*new_path) and (new_path not in paths.keys() or paths[new_path] > steps + 1) and all(j >= 0 for j in new_path):
                paths[new_path] = steps + 1
        closed_paths.add(path)

    return len(closed_paths)


print(part1())
print(part2())