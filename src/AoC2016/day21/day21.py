with open("input.txt", "r") as f:
    input = [i.split(" ") for i in f.read().splitlines()]

def solve(inp, part2 = False): # todo: funkce, parametr "reverse"
    res = inp
    if part2:
        l = input[::-1]
    else:
        l = input
    for i in l:
        if i[0] == "swap":
            if i[1] == "position":
                res = list(res)
                res[int(i[2])], res[int(i[5])] = res[int(i[5])], res[int(i[2])]
                res = "".join(res)
            elif i[1] == "letter":
                res = res.replace(i[2], ".")
                res = res.replace(i[5], ",")
                res = res.replace(".", i[5])
                res = res.replace(",", i[2])
        elif i[0] == "rotate":
            if i[1] == "based":
                x = i[6]
                ind = res.index(x)
                rot = 1 + ind
                if ind >= 4:
                    rot += 1
                rot %= len(res)
                rot = len(res) - rot
                res = res[rot:] + res[:rot]
            else:
                x = int(i[2]) % len(res)
                if i[1] == "left":
                    res = res[x:] + res[:x]
                elif i[1] == "right":
                    x = len(res) - x
                    res = res[x:] + res[:x]
        elif i[0] == "reverse":
            s = int(i[2])
            e = int(i[4]) + 1
            res = res[:s] + res[s:e][::-1] + res[e:]
        elif i[0] == "move":
            x = res[int(i[2])]
            y_i = int(i[5])
            res = res.replace(x, "")
            res = res[:y_i] + x + res[y_i:]
    return res

print(solve("abcdefgh"))
print(solve("fbgdceah", True))