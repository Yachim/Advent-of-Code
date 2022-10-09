def get_power_level(x: int, y: int, serial_num: int) -> int:
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_num
    power_level *= rack_id
    power_level = int(str(power_level)[-3])
    power_level -= 5

    return power_level

def part1(inp):
    coords = []
    for x in range(1, 299):
        for y in range(1, 299):
            power_level = 0
            for x_ in range(x, x + 3):
                for y_ in range(y, y + 3):
                    power_level += get_power_level(x_, y_, inp)

            coords.append([f"{x},{y}", power_level])

    return max(coords, key=lambda x: x[1])[0]

def part2(inp):
    raise NotImplementedError()
    
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = int(f.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")