input = open("input.txt", "r").read()

def part1():
    coords = [0,0]
    delivered_coords = [(0,0)]
    for i in input:
        coords[0] += {"^": 0, "v": 0, ">": 1, "<": -1}[i]
        coords[1] += {"^": 1, "v": -1, ">": 0, "<": 0}[i]
        delivered_coords.append(tuple(coords))
    return len(set(delivered_coords))

def part2():
    coords = [0,0]
    robot_coords = [0,0]
    delivered_coords = [(0,0), (0,0)] # both santa and robot deliver here. useless in the end...
    for i in range(len(input)):
        if i%2 == 0:
            coords[0] += {"^": 0, "v": 0, ">": 1, "<": -1}[input[i]]
            coords[1] += {"^": 1, "v": -1, ">": 0, "<": 0}[input[i]]
            delivered_coords.append(tuple(coords))
        else:
            robot_coords[0] += {"^": 0, "v": 0, ">": 1, "<": -1}[input[i]]
            robot_coords[1] += {"^": 1, "v": -1, ">": 0, "<": 0}[input[i]]
            delivered_coords.append(tuple(robot_coords))
    return len(set(delivered_coords))

print(part1())
print(part2())