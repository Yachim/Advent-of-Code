# Things I've learned
List of all the things I've learned while solving this year
## Python specific
Specific to the python programing language, like functions and libraries.
### map(func, *iterables)
Returns map object. Applies function `func` to all elements of iterables.
```python
>>> list(map(int, ["1", "2", "3"]))
[1,2,3]
```

### enumerate(iterable, start)
Iterates through iterable and keeps count of the items. The argument `start` sets the starting number of the counter (default at 0).
```python
>>> for i, j in enumerate(["a", "b", "c"]):
...     print(i, j)
... 
0 a
1 b
2 c
```

### collections.Counter(iter)
Returns count of all items in an iterable.
```python
>>> cnt = collections.Counter("abcda")
>>> dict(cnt)
{'a': 2, 'b': 1, 'c': 1, 'd': 1}
```
#### most_common(n)
Returns the n most common items.
```python
>>> cnt.most_common(2)
[('a', 2), ('b', 1)]
```

### itertools.combinations(iter, n)
Returns combinations of iterable `iter`. Each combinations has a length of n (defaul is length of iterable).

### itertools.permutations(iter, n)
Returns permutations of iterable `iter`. Each combinations has a length of n (defaul is length of iterable).

### The difference between list, tuple and set
 - list:
   - ✔️ is mutable 
   - ✔️ is ordered
   - ✔️ supports indexing or slicing
   - ✔️ allows duplicate elements
 - tuple:
   - ❌ is immutable
   - ✔️ is ordered
   - ✔️ supports indexing or slicing
   - ✔️ allows duplicate elements
 - set:
   - ✔️ is mutable
   - ❌ is not ordered
   - ❌ doesn't support indexing or slicing
   - ❌ doesn't allow duplicate elements
#### frozenset
Immutable version of set. Can be an element of a set (normal set can't).

### set(a) ^ set(b)
Returns symmetric difference from sets a and b.
```python
>>> a = set([1,2,3])
>>> b = set([2,3,4])
>>> a ^ b
{1, 4}
```

### operator library 
Contains functions working as operatos, for example `operator.add(x, y)` is the same as `x + y`.
```python
>>> operator.add(1,2)
3
```

### functools.reduce(func, iter)
Applies the function `func` from left to right on all elements, reducing it to one value. Functions from the operator library can be passed. 
```python
>>> reduce(operator.mul, [1,2,3,4,5])
120
```

## General
Not specific to any programming language, like algorithms.
### Game of life optimalization
Suppose we have this 3x3 table for game of life:
|---|---|---|
|1|2|3|
|4|5|6|
|7|8|9|
When checking for neighbors, we have to check if it is an edge (or a corner) element, so we don't get an index out of range.
To avoid these checks a table like this can be used:
|---|---|---|---|---|
|a|b|c|d|e|
|p|1|2|3|f|
|o|4|5|6|g|
|n|7|8|9|h|
|m|l|k|j|i|
We can then use 1-9 as our playing area. Cells a-p always remain 0 (turned off) and we only use them for checks.

### Graph algorithms
#### DFS
#### BFS
#### Dijkstra's algorithm
#### A*
