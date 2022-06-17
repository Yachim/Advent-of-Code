import re

input = open("input.txt", "r").read().splitlines()

RE = "^(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.$"

stats = {}
for i in input:
    match = re.match(RE, i)
    stats[match.group(1)] = [int(match.group(2)), int(match.group(3)), int(match.group(4))] # [speed, duration, pause]

def part1():
    distances = []
    for i in stats:
        cycle_duration = stats[i][1] + stats[i][2] # duration of one cycle
        cycles = 2503 // cycle_duration # number of cycles
        cycles_duration = cycles * cycle_duration #duration of all cycles combined
        secs = cycles * stats[i][1] # time spent flying
        remaining_secs = 2503-cycles_duration
        if remaining_secs // stats[i][1] == 0:
            distances.append(secs * stats[i][0] + remaining_secs * stats[i][0]) # no need to include resting - only flying will be done
        else:
            distances.append(secs * stats[i][0] + stats[i][1] * stats[i][0])
    return max(distances)

def part2():
    scores = {} # and distances {name: [distance, score, running, time_running, time_resting]}
    for i in stats:
        scores[i] = [0, 0, True, 0, 0]
    for i in range(2503):
        for j in stats:
            if scores[j][2]:
                scores[j][0] = scores[j][0] + stats[j][0]
                scores[j][3] = scores[j][3] + 1
            else:
                scores[j][4] = scores[j][4] + 1

            if scores[j][3] == stats[j][1]:
                scores[j][2] = False
                scores[j][3] = 0
            elif scores[j][4] == stats[j][2]:
                scores[j][2] = True
                scores[j][4] = 0
        winning = max(scores, key=lambda x: scores[x][0])
        for j in scores:
            if scores[j][0] == scores[winning][0]:
                scores[j][1] = scores[j][1] + 1
    return scores[max(scores, key=lambda x: scores[x][1])][1]

print(part1())
print(part2())