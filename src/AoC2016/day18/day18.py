with open("input.txt", "r") as f:
    input = f.read()

first_row = [True] + [True if i == "." else False for i in input] + [True] # True = safe

def solve(row_cnt):
    cnt = first_row.count(True) - 2
    prev_row = first_row
    for i in range(row_cnt - 1):
        next_row = []
        for j in range(1, len(prev_row) - 1):
            if not prev_row[j - 1] == prev_row[j + 1]: # if only one of them false, center does not matter
                next_row.append(False)
            else:
                next_row.append(True)
        cnt += next_row.count(True)
        prev_row = [True] + next_row.copy() + [True]
    
    return cnt

print(solve(40))
print(solve(400000))