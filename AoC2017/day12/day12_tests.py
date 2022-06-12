from day12 import *

with open("test_input.txt", "r") as f:
    raw_in = f.read()
tests_passed = False

# input processing:
try:
    assert process_input(raw_in) == {
        0: {2},
        1: {1},
        2: {0, 3, 4},
        3: {2, 4},
        4: {2, 3, 6},
        5: {6},
        6: {4, 5}
    }
except AssertionError:
    print("input processing test NOT passed")
    tests_passed = False
else: 
    print("input processing tests passed")
    tests_passed = True

# part 1
try:
    out = part1(process_input(raw_in))
    assert out == 6, out
except AssertionError:
    print("part 1 tests NOT passed")
    tests_passed = False
else: 
    print("part 1 tests passed")
    tests_passed = True

# part 2
try:
    out = part2(process_input(raw_in))
    assert out == 2, out
except AssertionError as e:
    print(f"part 2 tests NOT passed; value: {e}")
    tests_passed = False
else: 
    print("part 2 tests passed")
    tests_passed = True


if tests_passed: 
    print("\nall tests passed")