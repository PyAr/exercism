class Point:
    def __init__(self, x, y):
        """Initialize Point object with x and y coordinates."""
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Check if two Point objects are equal."""
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        """Return string representation of Point object."""
        return f"Point(x={self.x}, y={self.y})"


class WordSearch:
    def __init__(self, puzzle):
        """Initialize WordSearch object with puzzle."""
        self.puzzle = puzzle

    def search(self, word):
        """Search for the word in all possible directions."""
        return (
            self.left_to_right_search(word)
            or self.right_to_left_search(word)
            or self.up_to_down_search(word)
            or self.down_to_up_search(word)
            or self.top_right_to_bottom_left_search(word)
            or self.bottom_left_to_top_right_search(word)
            or None
        )

    def left_to_right_search(self, word):
        """Search for the word from left to right in puzzle rows."""
        for y, row in enumerate(self.puzzle):
            if word in row:
                x1 = row.find(word)
                x2 = x1 + len(word) - 1
                return (Point(x1, y), Point(x2, y))

    def right_to_left_search(self, word):
        """Search for the word from right to left in puzzle rows."""
        for y, row in enumerate(self.puzzle):
            row = "".join(reversed(row))
            if word in row:
                x1 = len(row) - row.find(word) - 1
                x2 = x1 - len(word) + 1
                return (Point(x1, y), Point(x2, y))

    def up_to_down_search(self, word):
        """Search for the word from top to bottom in puzzle columns."""
        columns = zip(*self.puzzle)
        for x, column in enumerate(columns):
            column = "".join(column)
            if word in column:
                y1 = column.find(word)
                y2 = y1 + len(word) - 1
                return (Point(x, y1), Point(x, y2))

    def down_to_up_search(self, word):
        """Search for the word from bottom to top in puzzle columns."""
        columns = zip(*self.puzzle)
        for x, column in enumerate(columns):
            column = "".join(reversed(column))
            if word in column:
                y1 = len(column) - column.find(word) - 1
                y2 = y1 - len(word) + 1
                return (Point(x, y1), Point(x, y2))

    def top_right_to_bottom_left_search(self, word):
        """Search for the word diagonally from top right to bottom left."""
        for y in range(0, len(self.puzzle) - len(word)):
            for x in range(0, len(self.puzzle[0]) - len(word)):
                chars = []
                for i in range(len(word)):
                    chars.append(self.puzzle[y + i][x + i])
                diag = "".join(chars)
                if word in diag:
                    i1 = diag.find(word)
                    i2 = i1 + len(word) - 1
                    return (Point(x + i1, y + i1), Point(x + i2, y + i2))
                diag = "".join(reversed(diag))
                if word in diag:
                    i1 = len(diag) - diag.find(word) - 1
                    i2 = i1 - len(word) + 1
                    return (Point(x + i1, y + i1), Point(x + i2, y + i2))

    def bottom_left_to_top_right_search(self, word):
        """Search for the word diagonally from bottom left to top right."""
        for y in range(len(word) - 1, len(self.puzzle)):
            for x in range(0, len(self.puzzle[0]) - len(word)):
                chars = []
                for i in range(len(word)):
                    chars.append(self.puzzle[y - i][x + i])
                diag = "".join(chars)
                if word in diag:
                    i1 = diag.find(word)
                    i2 = i1 + len(word) - 1
                    return (Point(x + i1, y - i1), Point(x + i2, y - i2))
                diag = "".join(reversed(diag))
                if word in diag:
                    i1 = len(diag) - diag.find(word) - 1
                    i2 = i1 - len(word) + 1
                    return (Point(x + i1, y - i1), Point(x + i2, y - i2))
