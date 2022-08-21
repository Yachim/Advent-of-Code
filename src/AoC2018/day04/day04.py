from collections import Counter
from doctest import OutputChecker


def process_input(raw_in):
    inp = [i.split(" ") for i in raw_in.splitlines()]
    inp.sort(key=lambda x: "".join([x[0], x[1]]))

    out = {}
    last_guard = None
    for i in inp:
        if i[2] == "Guard":
            last_guard = int(i[3][1:]) # [1:] because there's "#"
            if last_guard not in out:
                out[last_guard] = []
        elif i[2] == "falls":
            out[last_guard].append(" ".join([i[0][1:], i[1][:-1]]))
        elif i[2] == "wakes":
            out[last_guard][-1] += "..." + " ".join([i[0][1:], i[1][:-1]])

    return out
        

def get_minutes(rng: str) -> int:
    fell_asleep, woke_up = rng.split("...")

    fell_asleep_minutes = int(fell_asleep.split(" ")[1].split(":")[1])
    woke_up_minutes = int(woke_up.split(" ")[1].split(":")[1])

    return woke_up_minutes - fell_asleep_minutes

def get_minutes_asleep(rng: str) -> list[int]:
    fell_asleep, woke_up = rng.split("...")

    fell_asleep_minutes = int(fell_asleep.split(" ")[1].split(":")[1])
    woke_up_minutes = int(woke_up.split(" ")[1].split(":")[1])

    return list(range(fell_asleep_minutes, woke_up_minutes))


def solve(inp, part2 = False):
    minutes = {}
    for i in inp:
        minutes[i] = {
            "sleeping": [k for j in inp[i] for k in get_minutes_asleep(j)]
        }

        if len(minutes[i]["sleeping"]) == 0:
            minutes[i]["max_minute"] = (0,0)
            minutes[i]["total"] = 0
            continue

        if part2:
            minutes[i]["max_minute"] = Counter(minutes[i]["sleeping"]).most_common(1)[0]
        else:
            minutes[i]["total"] = sum(get_minutes(j) for j in inp[i])

    if not part2:
        target_guard = max(minutes, key=lambda x: minutes[x]["total"])
        max_minutes = Counter(minutes[target_guard]["sleeping"]).most_common(1)[0][0] 
        return target_guard * max_minutes

    target_guard = max(minutes, key=lambda x: minutes[x]["max_minute"][1])
    return target_guard * minutes[target_guard]["max_minute"][0]

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = process_input(f.read())

    print(f"Part 1: {solve(inp)}")
    print(f"Part 2: {solve(inp, True)}")