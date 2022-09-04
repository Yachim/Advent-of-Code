class Node:
    metadata_cnt: int
    children_cnt: int
    metadata: list[int]
    children: list["Node"]

    def __init__(self, children_cnt: int, metadata_cnt: int, children: list["Node"], metadata: list[int]):
        self.metadata_cnt = metadata_cnt
        self.children_cnt = children_cnt
        self.metadata = metadata
        self.children = children

    def sum(self) -> int:
        s = sum(self.metadata)

        if self.children_cnt == 0: return s
        s += sum(i.sum() for i in self.children)

        return s

    def get_val(self) -> int:
        if self.children_cnt == 0: return sum(self.metadata)

        val = 0
        for i in self.metadata: 
            if i > self.children_cnt: continue

            val += self.children[i - 1].get_val()

        return val


def process_input(raw_in: str) -> Node:
    return create_tree([int(i) for i in raw_in.split(" ")])[0]

def create_tree(inp: list[int]) -> tuple[Node, list[int]]:
    children_cnt = inp[0]
    metadata_cnt = inp[1]
    inp = inp[2:]

    if children_cnt == 0:
        metadata = inp[:metadata_cnt]
        inp = inp[metadata_cnt:]

        node = Node(children_cnt, metadata_cnt, [], metadata)
        
        return (node, inp)

    children = []
    for _ in range(children_cnt):
        node, inp = create_tree(inp)
        children.append(node)

    metadata = inp[:metadata_cnt]
    inp = inp[metadata_cnt:]

    node = Node(children_cnt, metadata_cnt, children, metadata)

    return (node, inp)

def part1(tree: Node):
    return tree.sum()

def part2(tree: Node):
    return tree.get_val()

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = process_input(f.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")