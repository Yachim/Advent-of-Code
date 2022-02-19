input = open("input.txt", "r").read()
input = [int(i) for i in input.split("-")]

def part1():
    valid = 0
    for i in range(input[0], input[1]+1): 
        if any([str(i)[j] == str(i)[j+1] for j in range(5)]) and all([str(i)[j] <= str(i)[j+1] for j in range(5)]):
            valid += 1
    return valid

def part2():
    valid = 0
    for i in range(input[0], input[1]+1): 
        if any([str(i)[j] == str(i)[j+1] for j in range(5)]) and all([str(i)[j] <= str(i)[j+1] for j in range(5)]) and all([str(i).count(j) == 2 for j in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]]):
            valid += 1
    return valid
    

print(part1())
print(part2())