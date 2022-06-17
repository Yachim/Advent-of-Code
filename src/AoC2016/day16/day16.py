input = [True if i == "1" else False for i in open("input.txt", "r").read()]

def solve(target):
    inpt = input.copy()

    while len(inpt) < target:
        a = inpt
        b = [not i for i in reversed(inpt)]
        inpt = [*a, 0, *b]
    
    checksum = inpt[:target]
    while len(checksum) % 2 != 1:
        new_checksum = ""
        for i in range(0, len(checksum), 2):
            if checksum[i] == checksum[i + 1]:
                new_checksum += "1"
            else:
                new_checksum += "0"
        checksum = new_checksum
    return checksum

print(solve(272))
print(solve(35651584))