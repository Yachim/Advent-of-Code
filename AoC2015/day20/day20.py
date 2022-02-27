from math import sqrt

input = int(open("input.txt", "r").read())

def div_sum(n, part2=False):
    i = 1
    divs = set()
    while i <= sqrt(n):
        if n % i == 0:
            if part2 and n / i > 50:
                divs.add(int(n/i))
            else:
                divs.update((int(n/i), i))
        i += 1
    return sum(divs)

def part1():
    inpt = input / 10 
    i = 1
    while True:
        if div_sum(i) >= inpt:
            return i
        i += 1
        
def part2():
    inpt = input / 10 
    i = 1
    while True:
        if div_sum(i, True) >= inpt:
            return i
        i += 1

print(part2())