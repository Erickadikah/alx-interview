#!/usr/bin/python3
"""
    Island parameter
    0 rep water
    1 rep land
    cell connected horizontally
"""


def island_perimeter(grid):
    """Args: grid
    Return: perimeter island in Grid
    """
    # if not grid or not grid[0]:
    #     return 0;

    #getting rows from the grid
    rows = len(grid)
    perimeter = 0

    for row in range(rows):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                ##assuing the current cell contributes 4 to the perimeter
                perimeter += 4
                # print(perimeter)
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
