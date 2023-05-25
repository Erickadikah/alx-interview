# Island Parameter

## Description

Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

1 : represents a part of the island
0 : represents a water zone

Grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).

## Usage

test files are located in [tests](./tests):

```ptyhon
0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0]
    ]
    print(island_perimeter(grid))
```
