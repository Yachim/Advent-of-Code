import hashlib

input = open("input.txt", "r").read()

def part1():
    num = 0
    while True:
        hash = hashlib.md5(str.encode(input+str(num))).hexdigest()
        if hash[:5] == "00000":
            return num
        num+=1
        
def part2():
    num = 0
    while True:
        hash = hashlib.md5(str.encode(input+str(num))).hexdigest()
        if hash[:6] == "000000":
            return num
        num+=1


print(part1())
print(part2())