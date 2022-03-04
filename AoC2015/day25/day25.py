from msilib import sequence
import re

row, col = (int(i) for i in re.findall(r"^[\w ,.]+ (\d+),[\w ,]+ (\d+).$", open("input.txt", "r").read())[0])
row = 6
col = 6
a = col + row - 2 # side of the previous full triangle
triangle = a * (a+1) / 2 # area of the previous full triangle
target_index = int(triangle + col)
base = 20151125
factor = 252533
div = 33554393
seq = [base, base * factor % div]
while seq[-1] != base:
    seq.append(seq[-1] * factor % div)
seq.pop()

def part1():
    return seq[target_index % len(seq)]

print(part1())