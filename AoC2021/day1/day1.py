test = False

file_name = "input.txt" if not test else "testInput.txt"
input = open(file_name, "r").read().splitlines()

def part1():
    larger = 0
    for i in range(len(input)-1):
        if int(input[i+1]) > int(input[i]):
            larger+=1

    return larger

def part2():
    entries = []
    larger = 0

    for i in range(len(input)-2):
        entries.append(int(input[i])+int(input[i+1])+int(input[i+2]))

    for i in range(len(entries)-1):
        if int(entries[i+1]) > int(entries [i]):
            larger+=1
        
    return larger

print(part1())
print(part2())