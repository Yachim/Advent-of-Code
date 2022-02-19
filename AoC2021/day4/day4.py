test = True

file_name = "input.txt" if not test else "testInput.txt"
input = open(file_name, "r").read()
input = input.replace("  ", ",")
input = input.replace(" ", ",")
input = input.split("\n\n")
numbers = input[0].split(",")
input = [i.splitlines() for i in input[1:]]
input = [[i.split(",") for i in j] for j in input]
for i in range(len(input)): #desky (i=deska)
    for j in range(len(input[i])): #řádky (j=řádek)
        dict_ = {}
        for k in range(5): #sloupce (k=číslo)
            if input[i][j][k] == "":
                input[i][j].pop(k)
                #input[i][j][k] = {input[i][j][k]:0}
                dict_[input[i][j][k]] = 0
            else:
                #input[i][j][k] = {input[i][j][k]:0}
                dict_[input[i][j][k]] = 0
        input[i][j] = dict_
_input = input

def validate_board():
    for i in _input: #desky (i=deska)
        for j in i: #řádky (j=řádek)
            if list(j.values()) == [1,1,1,1,1]:
                return i
        for j in range(5):
            vals = [list(i[k].values())[j] for k in range(5)]
            if vals == [1,1,1,1,1]:
                return i

    return

def part1():
    index = 0
    while validate_board() == None:
        for i in range(len(_input)):
            for j in range(len(_input)):
                for k in list(_input[i][j].keys()):
                    if numbers[index] == k:
                        _input[i][j][k] = 1

        index+=1
    
    table = validate_board()
    sum = 0
    for i in table:
        for key, val in i.items():
            if val == 0:
                sum+=int(key)
    return sum*int(numbers[index])

def part2():
    pass
    

print(part1())
print(part2())