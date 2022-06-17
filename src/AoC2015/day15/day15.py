from itertools import combinations_with_replacement
import re

input = """Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8"""
RE = re.compile(r"(\w+): capacity (-*\d), durability (-*\d+), flavor (-*\d+), texture (-*\d*), calories (-*\d+)")

ingredients = {}
for i in RE.finditer(input):
    ingredients[i.group(1)] = [int(i.group(2)), int(i.group(3)), int(i.group(4)), int(i.group(5)), int(i.group(6))] # capacity, durability, flavor, texture, calories

combs = list(combinations_with_replacement(ingredients, 100))

def part1():
    props = []
    for i in combs:
        capacity = sum(ingredients[j][0] for j in i)
        capacity = 0 if capacity < 0 else capacity 
        durability = sum(ingredients[j][1] for j in i)
        durability = 0 if durability < 0 else durability 
        flavor = sum(ingredients[j][2] for j in i)
        flavor = 0 if flavor < 0 else flavor
        texture = sum(ingredients[j][3] for j in i)
        texture = 0 if texture < 0 else texture
        props.append(capacity * durability * flavor * texture)
    return max(props)

def part2():
    props = []
    for i in combs:
        calories = sum(ingredients[j][4] for j in i)
        calories = 0 if calories < 0 else calories # it should never reach negative value
        if calories != 500:
            continue
        capacity = sum(ingredients[j][0] for j in i)
        capacity = 0 if capacity < 0 else capacity 
        durability = sum(ingredients[j][1] for j in i)
        durability = 0 if durability < 0 else durability 
        flavor = sum(ingredients[j][2] for j in i)
        flavor = 0 if flavor < 0 else flavor
        texture = sum(ingredients[j][3] for j in i)
        texture = 0 if texture < 0 else texture
        props.append(capacity * durability * flavor * texture)
    return max(props)

print(part1())
print(part2())