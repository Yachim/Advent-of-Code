import re

row, col = (int(i) for i in re.findall(r"^[\w ,.]+ (\d+),[\w ,]+ (\d+).$", open("input.txt", "r").read())[0])
row = 6
col = 1
a = col + row - 2 # side of the previous full triangle
triangle = a * (a+1) / 2 # area of the previous full triangle
target_index = int(triangle + col)


# část odsud nefunguje
base = 20151125
factor = 252533
div = 33554393
val = (base * factor) % div
base_i = 1
while val != base:
    base_i += 1
    val = (val * factor) % div

def part1():
    val = base
    for i in range(target_index % base_i):
        val = (val * factor) % div
    return val

print(part1())