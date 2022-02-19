input = [i.split(" contain ") for i in open("testInput.txt", "r").read().splitlines()]
values = {}
for i in input:
    i[0] = i[0].replace(" bags", "")
    input[input.index(i)][1] = i[1].replace(".", "")
    input[input.index(i)][1] = i[1].replace(" bags", "")
    input[input.index(i)][1] = i[1].replace(" bag", "")
    input[input.index(i)][1] = i[1].split(", ")
for i in input:
    if i[1][0] != "no other":
        values[i[0]] = {j[2:]:int(j[0]) for j in i[1]}
    else:
        values[i[0]] = None

def part1():
    queue = ["shiny gold"]
    visited = []
    while queue:
        for i in values.keys():
            if values[i] != None:
                for j in values[i].keys():
                    if j in queue and i not in queue:
                        queue.append(i)
                        visited.append(i)
        queue.pop(0)
    return len(set(visited))

def part2(param):
    finished = False
    count = 0
    

print(part1())
print(part2("shiny gold"))