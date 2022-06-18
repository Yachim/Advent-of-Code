from concurrent.futures import process
from functools import reduce
from typing import Tuple
import numpy as np


def process_input(raw_str: str) -> Tuple[int]:
    return tuple(int(i) for i in raw_str.split(","))

def ascii_conversion(s):
    return [ord(str(i)) for i in s] + [17,31,73,47,23]

def knot(lengths, l, index=0, skip=0):
    for i in lengths:
        if i > len(l):
            continue

        section = np.take(l, range(index, index + i), mode="wrap")
        np.put(l, range(index, index + i), np.flip(section), mode="wrap")

        index += skip + i
        skip += 1

    return l, index, skip

def create_dense_hash(l):
    hash = []
    for i in range(0, len(l), 16):
        hash.append(reduce(lambda x, y: x ^ y, l[i:i+16]))
    
    return hash

def create_hex(l):
    s = ""
    for i in l:
        h = hex(i)[2:]
        if len(h) != 2:
            h = "0" + h

        s += h

    return s


def part1(list_len: int, lengths: Tuple[int]):
    l = knot(lengths, np.arange(list_len))[0]  

    return l[0] * l[1]

def part2(list_len: int, lengths: Tuple[int]):
    l = np.arange(list_len)
    index = 0
    skip = 0
    lengths = ascii_conversion(lengths)
    for _ in range(64):
        [l, index, skip] = knot(lengths, l, index, skip)

    dense_hash = create_dense_hash(l)

    return create_hex(dense_hash)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_text = f.read()

    print(part1(256, process_input(input_text)))
    print(part2(256, input_text))