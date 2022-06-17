from copy import deepcopy
import re

input = open("input.txt", "r").read().splitlines()

RE_FLOORS = r"(\w+)( generator|-compatible microchip)"
TYPES = {" generator": "g", "-compatible microchip": "m"}

floors = []
for i in input:
    floor = []
    for j in re.finditer(RE_FLOORS, i):
        floor.append(f"{j.group(1)}-{TYPES[j.group(2)]}")
    floors.append(floor)
things = set([j for i in floors for j in i])

PAIRS = {"-g": "-m", "-m": "-g"}
def check_floors(state):
    for i in state:
        gen_present = any([j[-1] == "g" for j in i])
        floor = []
        for j in i: 
            t = j[-2:]
            opposite = j[:-2] + PAIRS[t]
            if opposite not in i:
                floor.append(opposite)
        types = set(j[-1] for j in floor)
        if "m" in types and gen_present:
            return False

    return True

'''def part1():
    queue = {tuple(tuple(i) for i in floors):(0, 0)} # (steps, elevator_index)
    
    while True:
        state = min(queue, key=lambda x: queue[x][0]) # heurisrics: + (3 - queue[x][2])  ?
        steps = queue[state][0]
        floor_num = queue[state][1]
        queue.pop(state)
        state = [list(i) for i in state]

        for i in state[floor_num]:
            for j in (-1, 1):
                new_steps = steps + 1
                new_floor_num = floor_num + j
                if new_floor_num < 0 or new_floor_num > 3:
                    continue
                new_state = deepcopy(state)
                new_state[floor_num].remove(i)
                new_state[new_floor_num].append(i)

                new_state = tuple(tuple(k) for k in new_state)

                if len(new_state[0]) == 0 and len(new_state[1]) == 0 and len(new_state[2]) == 0:
                    return new_steps
                if check_floors(new_state) and (new_state not in queue or new_steps < queue[new_state][0]):
                    queue[new_state] = (new_steps, new_floor_num)'''

def part1():
    queue = {tuple(tuple(i) for i in floors):(0, 0)} # (steps, elevator_index)
    seen = set()
    
    while True:
        state = list(queue.keys())[0] 
        steps = queue[state][0]
        floor_num = queue[state][1]
        queue.pop(state)
        state = [list(i) for i in state]
        floor = state[floor_num]

        for i in floor:
            floor_ = [j for j in floor if j != i]
            for j in floor_:
                for k in (-1, 1):
                    new_steps = steps + 1
                    new_floor_num = floor_num + k
                    if new_floor_num < 0 or new_floor_num > 3:
                        continue
                    new_state = deepcopy(state)
                    new_state[floor_num].remove(i)
                    new_state[floor_num].remove(j)
                    new_state[new_floor_num].append(i)
                    new_state[new_floor_num].append(j)

                    new_state = tuple(tuple(k) for k in new_state)

                    if len(new_state[0]) == 0 and len(new_state[1]) == 0 and len(new_state[2]) == 0:
                        return new_steps
                    if check_floors(new_state) and (new_state not in queue or new_steps < queue[new_state][0]) and new_state not in seen:
                        queue[new_state] = (new_steps, new_floor_num)
                        seen.add(new_state) 
            for j in (-1, 1):
                new_steps = steps + 1
                new_floor_num = floor_num + j
                if new_floor_num < 0 or new_floor_num > 3:
                    continue
                new_state = deepcopy(state)
                new_state[floor_num].remove(i)
                new_state[new_floor_num].append(i)

                new_state = tuple(tuple(k) for k in new_state)

                if len(new_state[0]) == 0 and len(new_state[1]) == 0 and len(new_state[2]) == 0:
                    return new_steps
                if check_floors(new_state) and (new_state not in queue or new_steps < queue[new_state][0]) and new_state not in seen:
                    queue[new_state] = (new_steps, new_floor_num)
                    seen.add(new_state)              

print(part1())