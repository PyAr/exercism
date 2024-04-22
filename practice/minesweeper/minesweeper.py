def annotate(minefield):
    """
    Annotate a minefield with the number of mines each square is adjacent to.

    The minefield is represented as a list of strings. Each string represents a row of the minefield,
    with '*' representing a mine and ' ' representing an empty square.

    The function returns a new minefield where each empty square is replaced with the number of mines
    that square is adjacent to. If a square is adjacent to no mines, it is replaced with a space.

    Args:
        minefield (list): A list of strings representing the minefield.

    Returns:
        list: A list of strings representing the annotated minefield.

    Raises:
        ValueError: If the minefield is not a rectangle or contains invalid characters.

    Examples:
        >>> annotate([" * ", "   ", " * "])
        ['1*1', '232', '1*1']
    """
    # If the minefield is empty, return an empty list
    if not minefield:
        return []

    # Check if the minefield is a rectangle and contains only valid characters
    if not all(len(row) == len(minefield[0]) for row in minefield) or any(c not in ' *' for row in minefield for c in row):
        raise ValueError("The board is invalid with current input.")
    
    # Get the number of rows and columns in the minefield
    rows, cols = len(minefield), len(minefield[0])

    # Initialize a 2D list to store the counts of adjacent mines
    counts = [[0]*cols for _ in range(rows)]
    
    # For each square in the minefield, if it is a mine, increment the count of all adjacent squares
    for i in range(rows):
        for j in range(cols):
            if minefield[i][j] == '*':
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if 0 <= i+di < rows and 0 <= j+dj < cols:
                            counts[i+di][j+dj] += 1
    
    # Replace each count with a string, leaving mines as '*' and replacing 0 with ' '
    for i in range(rows):
        for j in range(cols):
            if minefield[i][j] == '*':
                counts[i][j] = '*'
            elif counts[i][j] == 0:
                counts[i][j] = ' '
            else:
                counts[i][j] = str(counts[i][j])
    
    # Join each row into a string and return the annotated minefield
    return [''.join(row) for row in counts]