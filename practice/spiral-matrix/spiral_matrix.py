"""
Spiral Matrix - spiral_matrix generates a square matrix of a given size in a spiral pattern.
It initializes a matrix with None values and then fills it with numbers in a spiral pattern.
The function uses itertools.cycle to iterate through a cycle of movement directions:
(0,1) for moving right, (1,0) for moving down, (0,-1) for moving left, and (-1,0) for moving up.
The matrix is filled in a spiral pattern by updating the current cell's position and direction 
based on the cycle and checking for boundaries and filled cells.
"""
 
from itertools import cycle
 
def spiral_matrix(size):
    matrix = [[None] * size for _ in range(size)]
    r, c = 0, 0
    # this cycle determines the movement of the "current cell"
    # (0,1) represents moving along a row to the right
    # (1,0) represents moving down a column
    deltas = cycle(((0,1), (1,0), (0,-1), (-1,0)))
    dr, dc = next(deltas)
    for i in range(size**2):
        matrix[r][c] = i+1
        if (
            not 0 <= r+dr < size or
            not 0 <= c+dc < size or
            matrix[r+dr][c+dc] is not None
        ):
            dr, dc = next(deltas)
        r += dr
        c += dc
    return matrix