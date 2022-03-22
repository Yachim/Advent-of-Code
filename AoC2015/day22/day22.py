input = tuple(int(i.split(" ")[-1]) for i in open("input.txt", "r").read().splitlines()) # (hp, dmg)]
plr_stats = (50, 0, 500) # hp, armor, mana

"""Magic Missile costs 53 mana. It instantly does 4 damage.
Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana."""

spell_list = ("m", "d", "s", "p", "r")

def solve(part2=False): 
    nodes = {(*plr_stats, *input, 0, 0, 0, 0): (0, "")} # {(0: plr_hp, 1: plr_armor, 2: plr_mana, 3: boss_hp, 4: boss_dmg, 5: timer_shield, 6: timer_poison, 7: timer_recharge, 8: spell_count): (0: mana_spent, 1: last_spell)}
    while nodes:
        node_data = min(nodes, key=lambda x: nodes[x][0]) #hp, damage, armor, timers
        node_stats = nodes.pop(node_data) # mana_spent, spells
        node_data = list(node_data)

        if part2:
            node_data[0] -= 1
            if node_data[0] <= 0:
                continue

        # effects at the start of player's turn
        if node_data[5] > 0:
            node_data[5] -= 1 # shield timer
        if node_data[6] > 0:
            node_data[6] -= 1 # poison timer
            node_data[3] -= 3 # dmg to boss
        if node_data[7] > 0:
            node_data[7] -= 1 # recharge timer
            node_data[2] += 101 # mana recharge

        if node_data[5] == 0:
            node_data[1] = 0 # shield reset

        if node_data[3] <= 0: # if boss is dead
                return node_stats[0], node_stats[1]

        for i in spell_list:
            node_data_ = node_data.copy()
            node_stats_ = list(node_stats)
            if i == "m" and node_data_[2] >= 53:
                node_data_[2] -= 53 # mana from player
                node_data_[3] -= 4 # dmg to boss
                node_stats_[0] += 53 # mana to mana spent
                node_stats_[1] += i
            elif i == "d" and node_data_[2] >= 73:
                node_data_[2] -= 73 # mana from player
                node_data_[3] -= 2 # dmg to boss
                node_data_[0] += 2 # hp to plr
                node_stats_[0] += 73 # mana to mana spent
                node_stats_[1] += i
            elif i == "s" and node_data_[2] >= 113 and node_data_[5] == 0:
                node_data_[2] -= 113 # mana from player
                node_data_[5] = 6 # timer
                node_data_[1] = 7 # plr shield
                node_stats_[0] += 113 # mana to mana spent
                node_stats_[1] += i
            elif i == "p" and node_data_[2] >= 173 and node_data_[6] == 0:
                node_data_[2] -= 173 # mana from player
                node_data_[6] = 6 # timer
                node_stats_[0] += 173 # mana to mana spent
                node_stats_[1] += i
            elif i == "r" and node_data_[2] >= 229 and node_data_[7] == 0:
                node_data_[2] -= 229 # mana from player
                node_data_[7] = 5 # timer
                node_stats_[0] += 229 # mana to mana spent
                node_stats_[1] += i
            else:
                continue

            # effects at the start of boss's turn
            if node_data_[5] > 0:
                node_data_[5] -= 1 # shield timer
            if node_data_[6] > 0:
                node_data_[6] -= 1 # poison timer
                node_data_[3] -= 3 # dmg to boss
            if node_data_[7] > 0:
                node_data_[7] -= 1 # recharge timer
                node_data_[2] += 101 # mana recharge
                
            if node_data_[5] == 0:
                node_data_[1] = 0 # shield reset

            if node_data_[3] <= 0: # if boss is dead
                return node_stats_[0], node_stats_[1] # more spell combinations are possible, like 'mprmpsmm' or 'rpmmpsmm'

            boss_dmg = node_data_[4] - node_data_[1]
            boss_dmg = 1 if boss_dmg <= 0 else boss_dmg
            node_data_[0] -= boss_dmg

            if not node_data_[2] < 53 and not node_data_[0] <= 0: # if the node is not loss - cannot cast a spell or player dead
                if tuple(node_data_) not in nodes.keys() or node_stats_[0] < nodes[tuple(node_data_)][0]: # if not in dictionary or mana_spent is lower
                    nodes[tuple(node_data_)] = tuple(node_stats_)

print(*solve())
print(*solve(True))