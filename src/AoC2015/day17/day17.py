input = list(map(int, open("input.txt", "r").read().splitlines()))

def solve(subset=[], remaining=input): # vraci none a 2. část nejspíš nemá fungovat
    if sum(subset) > 150:
        return
    elif sum(subset) == 150:
        yield subset
    for i, j in enumerate(remaining):
        yield from solve(subset+[j], remaining[i+1:])
       
print(len(list(solve())))
print(len(min(list(solve()), key=lambda x: len(x))))