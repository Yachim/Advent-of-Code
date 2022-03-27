# Things I've learned
List of all the things and skills I've learned and improved while solving this year
## Python-specific
Specific to the python programing language, like functions and libraries.
### Numpy arrays
#### numpy.zeros(tuple)
Creates array of zeros. Accepts tuple as a shape.
```python
>>> numpy.zeros((5,3))
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])
```

#### Slicing and indexing
Example array: 
```python
>>> arr = numpy.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
>>> arr
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]])
```
Indexing and slicing can be done in single square brackets:
```python
>>> arr[1, 0]
4
```
```python
>>> arr[1:3, :2]
array([[4, 5],
       [7, 8]])
```

#### roll(arr, shift, axis)
Roll shifts array `arr` by `shift` places with optional parameter `axis`. If `axis` is none it flattens the array. 
```python
>>> numpy.roll(arr, 1)
array([[12,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11]])
```
```python
>>> numpy.roll(arr, 1, 0)
array([[10, 11, 12],
       [ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9]])
>>> numpy.roll(arr, 1, 1)
array([[ 3,  1,  2],
       [ 6,  4,  5],
       [ 9,  7,  8],
       [12, 10, 11]])
```

## General
Not specific to any programming language, like algorithms.
### 
