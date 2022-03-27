from ast import Pass
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

def part1():
    queue = {tuple(tuple(i) for i in floors):(0, 0)} # (steps, elevator_index)
    
    while True:
        state = min(queue, key=lambda x: queue[x][0])
        steps = queue[state][0]
        floor_num = queue[state][1]

        new_state = [list(i) for i in state]
        current_floor = new_state[floor_num]
        for i in current_floor:
            pass

print(part1())