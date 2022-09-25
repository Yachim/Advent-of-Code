def part1(inp: int):
    recipes = "37"
    elf1_i = 0
    elf2_i = 1
    while len(recipes) < inp + 10:
        elf1_recipe = int(recipes[elf1_i])
        elf2_recipe = int(recipes[elf2_i])

        new_recipes = str(elf1_recipe + elf2_recipe)
        recipes += new_recipes

        elf1_i += 1 + elf1_recipe
        elf1_i %= len(recipes)
        elf2_i += 1 + elf2_recipe
        elf2_i %= len(recipes)


    recipes10 = recipes[inp:inp+10]
    return "".join(recipes10)

def part2(inp: int):
    recipes = "37"
    elf1_i = 0
    elf2_i = 1
    while str(inp) not in recipes[-7:]:
        elf1_recipe = int(recipes[elf1_i])
        elf2_recipe = int(recipes[elf2_i])

        new_recipes = str(elf1_recipe + elf2_recipe)
        recipes += new_recipes

        elf1_i += 1 + elf1_recipe
        elf1_i %= len(recipes)
        elf2_i += 1 + elf2_recipe
        elf2_i %= len(recipes)

    return recipes.index(str(inp))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = int(f.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")