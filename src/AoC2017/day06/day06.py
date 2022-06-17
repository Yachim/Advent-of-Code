import numpy as np


with open("input.txt", "r") as f:
    input = np.array(list(map(int, f.read().split("\t"))))

def solve(part2=False):
    inpt = input.copy()
    seen = []
    steps = 0
    cnt = len(inpt)
    while tuple(inpt) not in seen:
        seen.append(tuple(inpt))
        i = max(range(cnt), key=lambda x: (inpt[x], cnt-x))
        blocks_cnt = inpt[i]
        inpt[i] = 0
        
        portion = int(blocks_cnt / cnt)
        rem = blocks_cnt % cnt

        inpt += portion
        inpt[i+1:i+rem+1] += 1
        if i+rem+1 > cnt:
            inpt[:(i+rem+1-cnt)] += 1

        steps += 1

    if part2:
        return steps - seen.index(tuple(inpt))
    return steps


print(solve())
print(solve(True))