import re
from copy import deepcopy

RE_VALUES = r"value (\d+) goes to bot (\d+)"
RE_BOTS = r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)"

input = open("input.txt", "r").read()

bots = {f"bot{str(i.group(2))}":[] for i in re.finditer(RE_VALUES, input)} # bots and outputs
for i in re.finditer(RE_VALUES, input):
    bots[f"bot{str(i.group(2))}"].append(int(i.group(1)))

bot_instructions = {}
for i in re.finditer(RE_BOTS, input):
    bot_instructions[f"bot{str(i.group(2))}"] = (i.group(2), i.group(3), i.group(4), i.group(5))

def solve(part2=False):
    bots_ = deepcopy(bots)
    while "bot" in "".join(bots_.keys()):
        bot = max(bots_, key=lambda x: len(bots_[x]))
        instructions = bot_instructions[bot]
        low_receive = instructions[0] + instructions[1]
        high_receive = instructions[2] + instructions[3]
        high = max(bots_[bot])
        low = min(bots_[bot])

        if high == 61 and low == 17 and not part2:
            return bot

        if low_receive in bots_.keys():
            bots_[low_receive].append(low)
        else:
            bots_[low_receive] = [low]

        if high_receive in bots_.keys():
            bots_[high_receive].append(high)
        else:
            bots_[high_receive] = [high]
        bots_.pop(bot)
    return bots_["output0"][0] * bots_["output1"][0] * bots_["output2"][0]

print(solve())
print(solve(True))