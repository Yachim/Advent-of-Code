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

## General
Not specific to any programming language, like algorithms.
### Game of life optimalization