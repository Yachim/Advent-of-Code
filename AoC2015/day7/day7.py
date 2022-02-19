import re

input = open("input.txt", "r").read()

RE1 = r"^((NOT) )?([a-z]{1,2}|[0-9]{1,5}) (?:->) ([a-z]{1,2})$" # matches when there's "not" (optional) and output
RE2 = r"^([a-z]{1,2}|[0-9]{1,5}) (AND|OR|LSHIFT|RSHIFT) ([a-z]{1,2}|[0-9]{1,5}) (?:->) ([a-z]{1,2})$" # matches something like "12345 OR jb -> jc"
OP_DICT = {"AND": lambda x, y: x & y, "OR": lambda x, y: x | y, "RSHIFT": lambda x, y: x >> y, "LSHIFT": lambda x, y: x << y}

def part1():
    inpt = input.splitlines()
    wires = {}
    curr_index = 0
    while len(inpt) != 0:
        if curr_index >= len(inpt):
            curr_index = 0
        if re.match(RE1, inpt[curr_index]):
            res = re.search(RE1, inpt[curr_index])
            wire_input = res.group(3)
            wire_output = res.group(4)
            is_not = res.group(2)
            if wire_input.isnumeric():
                wires[wire_output] = int(wire_input) if is_not == None else int(~wire_input)
            else:
                if wire_input in wires:
                    wires[wire_output] = int(wires[wire_input]) if is_not == None else int(~wires[wire_input])
                else:
                    curr_index += 1
                    continue
        else:
            res = re.search(RE2, inpt[curr_index])
            wire_input1 = res.group(1)
            wire_input2 = res.group(3)
            wire_operator = res.group(2)
            wire_output = res.group(4)

            if not wire_input1.isnumeric():
                if wire_input1 in wires:
                    wire_input1 = wires[wire_input1]
                else:
                    curr_index += 1
                    continue
            wire_input1 = int(wire_input1)
            if not wire_input2.isnumeric():
                if wire_input2 in wires:
                    wire_input2 = wires[wire_input2]
                else:
                    curr_index += 1
                    continue
            wire_input2 = int(wire_input2)
            wires[wire_output] = int(OP_DICT[wire_operator](wire_input1, wire_input2))
        inpt.pop(curr_index)
    return wires["a"]

def part2():
    wires = {"b": part1()}
    inpt = input.splitlines()
    curr_index = 0
    while len(inpt) != 0:
        if curr_index >= len(inpt):
            curr_index = 0
        if re.match(RE1, inpt[curr_index]):
            res = re.search(RE1, inpt[curr_index])
            wire_input = res.group(3)
            wire_output = res.group(4)
            is_not = res.group(2)
            if wire_input.isnumeric():
                if wire_output != "b":
                    wires[wire_output] = int(wire_input) if is_not == None else int(~wire_input)
            else:
                if wire_input in wires and wire_output != "b":
                    wires[wire_output] = int(wires[wire_input]) if is_not == None else int(~wires[wire_input])
                else:
                    curr_index += 1
                    continue
        else:
            res = re.search(RE2, inpt[curr_index])
            wire_input1 = res.group(1)
            wire_input2 = res.group(3)
            wire_operator = res.group(2)
            wire_output = res.group(4)

            if not wire_input1.isnumeric():
                if wire_input1 in wires:
                    wire_input1 = wires[wire_input1]
                else:
                    curr_index += 1
                    continue
            wire_input1 = int(wire_input1)
            if not wire_input2.isnumeric():
                if wire_input2 in wires:
                    wire_input2 = wires[wire_input2]
                else:
                    curr_index += 1
                    continue
            wire_input2 = int(wire_input2)
            if wire_output != "b":
                wires[wire_output] = int(OP_DICT[wire_operator](wire_input1, wire_input2))
        inpt.pop(curr_index)
    return wires["a"]

print(part1())
print(part2())