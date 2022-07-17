import numpy as np

def process_elem(el: str):
    el_dict = {"type": el[0]}
    if el_dict["type"] == "s":
        el_dict.update({
            "size": int(el[1:])
        })
    elif el_dict["type"] in ["x", "p"]:
        first, second = el[1:].split("/")

        if el_dict["type"] == "x":
            first = int(first)
            second = int(second)

        el_dict.update({
            "first": first,
            "second": second,
        })
    else:
        raise ValueError("Invalid type")
    
    return el_dict

def process_input(raw_inp: str):
    return map(process_elem, raw_inp.split(","))

def solve(dance: str, part2=False):
    dance = process_input(dance)
    commands = np.array(list("abcdefghijklmnop"))

    iters = 1_000_000_000 if part2 else 1
    dance = list(dance) if part2 else dance

    # this has to be optimized by finding where the array (commands) are the same as the beginning and then running only the next commands
    for _ in range(iters):
        for i in dance:
            if i["type"] == "s":
                commands = np.roll(commands, i["size"])
            elif i["type"] in ["x", "p"]:
                first = i["first"]
                second = i["second"]

                if i["type"] == "p":
                    first = np.where(commands == first)[0]
                    second = np.where(commands == second)[0]

                commands[first], commands[second] = commands[second], commands[first]

    return "".join(commands)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = f.read()

    print(f"Part 1: {solve(inp)}")
    print(f"Part 2: {solve(inp, True)}")