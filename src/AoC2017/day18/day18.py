def process_input(raw: str):
    ins = []
    regs = set()
    for i in raw.splitlines():
        i = i.split(" ")
        instruction = {"in": i[0], "reg": i[1]}
        if len(i) > 2:
            try:
                instruction["val"] = int(i[2])
            except ValueError:
                instruction["val"] = i[2]
        ins.append(instruction)
        regs.update(j for j in list(instruction.values())[1:] if not isinstance(j, int) and not j[0] == "-" and not j.isnumeric())

    return (ins, regs)

def part1(instructions, regs):
    regs = {
        i: {
            "val": 0, 
            "last_freq": None
        } for i in regs
    }
    current_i = 0
    
    while True:
        ins = instructions[current_i]
        cmd = ins["in"]

        reg = regs[ins["reg"]]

        try:
            val = ins["val"]
            val = val if isinstance(val, int) else regs[val]["val"]
        except KeyError:
            pass


        if cmd == "snd":
            reg["last_freq"] = reg["val"]
        elif cmd == "rcv" and reg["val"] != 0 and reg["last_freq"] != None:
            return reg["last_freq"]
        elif cmd == "set":
            reg["val"] = val
        elif cmd == "add":
            reg["val"] += val
        elif cmd == "mul":
            reg["val"] *= val
        elif cmd == "mod":
            reg["val"] %= val
        elif cmd == "jgz" and reg["val"] > 0:
            current_i += val
            continue
        
        current_i += 1    

def part2(instructions, regs):
    # queue_sent = queue of numbers pending for recv command
    # queue_recv = queue of registers pending for snd command from other program
    programs = [
        {
            "terminated": False, 
            "queue_recv": [], 
            "queue_sent": [], 
            "current_i": 0, 
            "regs": {
                i: {
                    "val": 0, 
                    "last_freq": None
                } for i in regs
            }
        } for _ in range(2)
    ]
    sent_cnt = 0

    while all(not i["terminated"] for i in programs):
        for i, p in enumerate(programs): 
            if p["current_i"] not in range(len(instructions)):
                p["terminated"] = True
                continue

            ins = instructions[p["current_i"]]
            cmd = ins["in"]
            reg_name = ins["reg"]
            try:
                reg = p["regs"][reg_name]
            except KeyError:
                reg = {"val": int(reg_name)} # because jgz sometimes can have numbers

            try:
                val = ins["val"]
                val = val if isinstance(val, int) else p["regs"][val]["val"]
            except KeyError:
                pass

            if cmd == "snd":
                other_i = 1 if i == 0 else 1
                other_program = programs[other_i]

                if len(other_program["queue_recv"]) > 0:
                    other_reg_name = other_program["queue_recv"].pop(0)
                    other_reg = other_program["regs"][other_reg_name]
                    other_reg["val"] = reg["val"]
                else: 
                    other_program["queue_sent"].insert(0, reg["val"])

                if i == 1: sent_cnt += 1
            elif cmd == "rcv" and reg["val"] != 0 and reg["last_freq"] != None:
                if len(p["queue_sent"]) > 0:
                    reg["val"] = p["queue_sent"].pop(0)
                else:
                    p["queue_recv"].insert(0, reg_name)
            elif cmd == "set":
                reg["val"] = val
            elif cmd == "add":
                reg["val"] += val
            elif cmd == "mul":
                reg["val"] *= val
            elif cmd == "mod":
                reg["val"] %= val
            elif cmd == "jgz" and reg["val"] > 0:
                p["current_i"] += val
                continue
        
            p["current_i"] += 1

    return sent_cnt


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        ins, regs = process_input(f.read())

    print(f"Part 1: {part1(ins, regs)}")
    print(f"Part 2: {part2(ins, regs)}")