def spiral_matrix(size):
    matrix = [[0]*size for _ in range(size)]
    
    num = 1
    row_start, row_end = 0, size - 1
    col_start, col_end = 0, size - 1
    
    while num <= size*size:
        # Fill the top row from left to right
        for i in range(col_start, col_end + 1):
            matrix[row_start][i] = num
            num += 1
        row_start += 1

        # Fill the right column from top to bottom
        for i in range(row_start, row_end + 1):
            matrix[i][col_end] = num
            num += 1
        col_end -= 1

        # Fill the bottom row from right to left
        for i in range(col_end, col_start - 1, -1):
            matrix[row_end][i] = num
            num += 1
        row_end -= 1

        # Fill the left column from bottom to top
        for i in range(row_end, row_start - 1, -1):
            matrix[i][col_start] = num
            num += 1
        col_start += 1

    return matrix
    pass

# My Approach ---->

# A while loop is used to fill the matrix in a spiral order. 
# The loop continues until num is greater than the total number of elements in the matrix (size * size)

# Inside the loop, four for loops are used to fill 
# the top row from left to right, 
# the right column from top to bottom, 
# the bottom row from right to left, 
# and the left column from bottom to top, respectively.
# After each for loop, the corresponding starting or ending index is updated to move towards the center of the matrix.

# After the while loop, the filled matrix is returned.