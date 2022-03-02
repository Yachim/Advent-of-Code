input = [i.split(" ")[-1] for i in open("input.txt", "r").read().splitlines()] # [Hit Points, Damage]

"""Magic Missile costs 53 mana. It instantly does 4 damage.
Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana."""

def mis(boss_stats, plr_stats):
    if plr_stats[2] >= 53:
        boss_stats[0] -= 4
        plr_stats[2] -= 53
        return (boss_stats, plr_stats)
    else:
        return

def drain(boss_stats, plr_stats):
    if plr_stats[2] >= 73:
        boss_stats[0] -= 2
        plr_stats[2] -= 73
        plr_stats[0] += 2
        return (boss_stats, plr_stats)
    else:
        return

def shield(boss_stats, plr_stats, timers):
    if plr_stats[2] >= 113:
        plr_stats[1] = 7
        plr_stats[2] -= 113
        timers["Shield"] = 6
        return (boss_stats, plr_stats, timers)
    else:
        return

def poison(boss_stats, plr_stats, timers):
    if plr_stats[2] >= 173:
        plr_stats[2] -= 173
        timers["Poison"] = 6
        return (boss_stats, plr_stats, timers)
    else:
        return

def recharge(boss_stats, plr_stats, timers):
    if plr_stats[2] >= 229:
        plr_stats[2] -= 229
        timers["Poison"] = 5
        return (boss_stats, plr_stats, timers)
    else:
        return

spells = {"Missile": mis, "Drain": drain, "Shield": shield, "Poison": poison, "Recharge": recharge}

def part1(boss_stats=input, plr_stats=[50, 0, 500], timers={"Shield": 0, "Poison": 0, "Recharge": 0}, mana_spent=0): # plr stats = [Hit Points, Armor, Mana]
    if boss_stats[0] <= 0:
        return mana_spent
    elif plr_stats[0] <= 0:
        return
    for i in timers:
        if timers[i] > 0:
            if i == "Shield":
                plr_stats[1] = 7
            elif i == "Poison":
                boss_stats -= 3
            elif i == "Recharge":
                plr_stats[2] += 101
            timers[i] -= 1
        else: 
            if i == "Shield":
                plr_stats[1] = 0
    for i in spells:
        if i in timers and timers[i] == 0:
            spell = spells[i]
            if spell:
                return part1(spell[0], spell[1], spell[2], mana_spent)
        else:
            pass

print(part1())