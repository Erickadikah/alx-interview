# Rotate 2D Matrix

## Problem Description

Given an `n x n` 2D matrix, rotate the matrix by 90 degrees (clockwise).

method: `def rotate_2d_matrix(matrix):`
n = len(matrix)

## first method

Transposing the matrix and then reversing each row.

```python

1  2  3  
4  5  6  
7  8  9

output:

1 4  7
2 5  8
3 6  9

reverse each row:

7 4 1
8 5 2
9 6 3

```

output:

```python
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]


```python
def rotate_2d_matrix(matrix):
    n = len(matrix)
    # transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # reverse each row
    for row in matrix:
        row.reverse()
```

## Author:bulb:

Erick Adikah - [Twitter: @erick_adikah](https://twitter.com/erick_adikah)
