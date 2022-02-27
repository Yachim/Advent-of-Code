import re 
from math import ceil

input = {i.group(1):int(i.group(2)) for i in re.finditer(r"([\w ]+): (\d+)", open("input.txt", "r").read())}

shop_in = [i.splitlines() for i in """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3""".split("\n\n")]

# {Weapons and Armor: (Cost, Damage, Armor), Rings: (Damage/Armor, Addition, Cost, Damage, Armor)}
shop = {} 
for i in shop_in[:2]:
    k = re.match(r"^(\w+): +Cost +Damage +Armor$", i[0]).group(1)
    shop[k] = [tuple(re.findall(r"(\d+)", j)) for j in i[1:]]
shop["Rings"] = sorted([re.findall(r"^(\w+) \+(\d) +(\d+) +(\d+) +(\d+)$", i)[0] for i in shop_in[2][1:]], key=lambda x: int(x[2]))

combs = set((100, int(i[1]), 0, int(i[0])) for i in shop["Weapons"]) # [(Hit Points, Damage, Armor, Cost)]
cs = combs.copy()
for i in shop["Armor"]:
    for j in cs:
        combs.add((100,  j[1], int(i[2]), int(i[0]) + j[3]))
ring_combs = set((int(i[3]), int(i[4]), int(i[2])) for i in shop["Rings"]) # (Damage, Armor, Cost)
cs = ring_combs.copy()
for i in shop["Rings"]:
    for j in cs:
        if int(i[3]) != j[0] and int(i[4]) != j[1]:
            ring_combs.add((int(i[3]) + j[0], int(i[4]) + j[1], int(i[2]) + j[2]))
cs = combs.copy()
for i in ring_combs:
    for j in cs:
        combs.add((100,  j[1] + int(i[0]), j[2] + int(i[1]), j[3] + int(i[2])))

def eval_fight(plr):
    plr_true_dmg = plr[1] - input["Armor"]
    boss_true_dmg = input["Damage"] - plr[2]
    if plr_true_dmg == 0:
        return False
    if boss_true_dmg == 0:
        return True
    plr_hits_needed = int(ceil(input["Hit Points"] / plr_true_dmg)) # number of hits the player needs to defeat the boss
    boss_hits_needed = int(ceil(plr[0] / boss_true_dmg)) # number of hits the boss needs to defeat the player 
    if plr_hits_needed <= boss_hits_needed:
        return True
    return False

def part1():
    prices = map(lambda y: y[3] if eval_fight(y) else 10000, combs)
    return min(prices)

def part2():
    prices = map(lambda y: y[3] if not eval_fight(y) else 0, combs)
    return max(prices)

print(part1())
print(part2())