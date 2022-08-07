import re

INPUT_RE = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", re.MULTILINE)

# [(claim, from_left_edge, from_top_edge, width, height)]
def process_input(raw_in):
    inp = []
    for i in INPUT_RE.finditer(raw_in):
        inp.append({
            "id": int(i.group(1)),
            "left": int(i.group(2)),
            "top": int(i.group(3)),
            "w": int(i.group(4)),
            "h": int(i.group(5))
        })

    return inp

def get_coords(left, top, w, h):
    coords = set()
    for i in range(w):
        for j in range(h):
            coords.add((left + i, top + j))

    return coords

def part1(inp):
    coords_taken = set()
    coords_registered = set()
    taken = 0
    for i in inp:
        coords = get_coords(i["left"], i["top"], i["w"], i["h"])
        for j in coords:
            if j in coords_taken and not j in coords_registered:
                taken += 1
                coords_registered.add(j)
        
        coords_taken.update(coords)

    return taken

def part2(inp):
    coords_taken = set()
    claims = set(i["id"] for i in inp)
    all_claims = claims.copy()
    for i in inp:
        coords = get_coords(i["left"], i["top"], i["w"], i["h"])
        for j in coords:
            for k in coords_taken:
                if not(k[0] == j[0] and k[1] == j[1] and k[2] in claims):
                    continue

                claims.remove(k[2])
                claims.remove(i["id"])
            coords_taken.add((*j, i["id"]))

    return list(claims)[0]

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = process_input(f.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")