input = open("input.txt", "r").read().split("\n\n")

ids = {}

def part1():
    valid = 0
    for i in input:
        if len([j for j in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] if j in i]) == 7:
            valid += 1
    return valid

def part2():
    valid = []
    for i in input:
        if len([j for j in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] if j in i]) == 7:
            valid.append(i)
    valid = [i.replace("\n", " ") for i in valid]
    valid = [i.split(" ") for i in valid]
    valid_dict = []
    for i in valid:
        dictionary = {}
        for j in i:
            dictionary.update({j[:j.index(":")]:j[j.index(":")+1:]})
        valid_dict.append(dictionary)
    valid_count = 0
    for i in valid_dict:
        if int(i["byr"]) in range(1920, 2003) \
            and int(i["iyr"]) in range(2010, 2021) \
            and int(i["eyr"]) in range(2020, 2031) \
            and (i["hgt"][-2:] == "cm" and int(i["hgt"][:-2]) in range(150, 194) \
                or i["hgt"][-2:] == "in" and int(i["hgt"][:-2]) in range(59, 77)) \
            and i["hcl"][0] == "#" and len([j for j in i["hcl"][1:] if j in["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]]) == 6  \
            and i["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] \
            and len(i["pid"]) == 9:
            valid_count += 1
    return valid_count


print(part1())
print(part2())