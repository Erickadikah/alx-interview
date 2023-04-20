# Pascal triangle

Pascal's triangle is a triangular array of the binomial coefficients. Write a function that returns a list of lists of integers representing the Pascal’s triangle of n.

```python

def pascal_triangle(n):

    """Returns a list of lists of integers representing the Pascal’s triangle of n"""

    if n <= 0:

        return []

    if n == 1:

        return [[1]]

    if n == 2:

        return [[1], [1, 1]]

    pascal = [[1], [1, 1]]

    for i in range(2, n):

        row = [1]

        for j in range(1, i):

            row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])

        row.append(1)

        pascal.append(row)

    return pascal

```

## Tasks

### 0. Pascal's Triangle

Write a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of n:

- Returns an empty list if n <= 0
- You can assume n will be always an integer

## Author

ERICK ADIKAH
