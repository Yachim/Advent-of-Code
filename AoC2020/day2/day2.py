input = open("input.txt", "r").read().splitlines()

def part1():
    valid = 0
    for i in input:
        lowest = int(i[:i.index("-")])
        most = int(i[i.index("-")+1:i.index(":")-1])
        letter = i[i.index(":")-1]
        password = i[i.index(":")+2:]
        if password.count(letter) >= lowest and password.count(letter) <= most:
            valid+=1
    return valid

def part2():
    valid = 0
    for i in input:
        lowest = int(i[:i.index("-")])
        most = int(i[i.index("-")+1:i.index(":")-1])
        letter = i[i.index(":")-1]
        password = i[i.index(":")+2:]
        if (password[lowest-1] == letter) ^ (password[most-1] == letter):
            valid+=1
    return valid

print(part1())
print(part2())