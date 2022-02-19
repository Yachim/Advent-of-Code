test = False

file_name = "input.txt" if not test else "testInput.txt"
input = open(file_name, "r").read()

def part1():
    _input = [list(i) for i in input.splitlines()]
    _input = list(zip(*_input))
    
    gamma = "" #max
    epsilon = "" #min
    for i in _input:
        if i.count("1") > i.count("0"):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    
    return int(gamma, 2)*int(epsilon,2)

def part2():
    _input = input.splitlines()

    oxygen = "" 
    co2 = ""
    index = 0
    while len(_input) > 1:
        arr = list(zip(*[list(i) for i in _input]))
        if arr[index].count("1") >= arr[index].count("0"):
            _input = list(filter(lambda x: x[index] == "1", _input))
        else:
            _input = list(filter(lambda x: x[index] == "0", _input))

        index+=1
    oxygen = _input[0]

    _input = input.splitlines()
    index = 0
    while len(_input) > 1:
        arr = list(zip(*[list(i) for i in _input]))
        if arr[index].count("0") > arr[index].count("1"):
            _input = list(filter(lambda x: x[index] == "1", _input))
        elif arr[index].count("0") == arr[index].count("1"):
            _input = list(filter(lambda x: x[index] == "0", _input))
        else:
            _input = list(filter(lambda x: x[index] == "0", _input))

        index+=1
    co2 = _input[0]

    return int(oxygen, 2)*int(co2, 2)
    

print(part1())
print(part2())