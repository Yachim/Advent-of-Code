from math import log2, log
import numpy as np

with open("input.txt") as f:
    input = int(f.read())
input = 6

def part1_binary():
    num = str(bin(input))[2:]
    return int(num[1:] + num[0], 2)

def part1():
    e = int(log2(input))
    rem = input - 2**e
    return 2*rem + 1

'''def part2_brute(): #semi-brute, too slow
    table = np.arange(1, input + 1)
    for i in range(len(table)):
        if log(len(table) - 1, 3).is_integer():
            return table[0]

        i = int(len(table)/2)
        table = np.delete(table, i)
        table = np.roll(table, -1)'''

'''def part2(): #semi-brute, too slow
    table = list(range(1, input + 1))
    num = 3**int(log(input, 3)) + 1

    if input == num - 1:
        return table[-1]
    while len(table) != num:
        index = int(len(table)/2)
        table.pop(index)
        table = table[1:] + [table[0]]
    
    return table[0]'''

'''def part2():
    plus = 2 if input % 2 else 1
    currently_removing = int(input / 2 + 1)
    for i in range(input):
        currently_removing += plus
        if plus == 2:
            plus = 1
        else:
            plus = 2
        if currently_removing > i:
            currently_removing -= input
    
    return currently_removing'''

'''def part2():
    e = int(log(input, 3))
    rem = input - 3**e
    return input - (3**e)'''


print(part1_binary())
print(part1())
#print(part2())
#print(part2())