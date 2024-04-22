WHITE = "W"
BLACK = "B"
NONE = " "
UNKNOWN = "?"

class Board:
    """Class to analyze territories in a Go game."""

    def __init__(self, board):
        """Initialize the Board instance with the given board configuration.

        Args:
            board (list[str]): A two-dimensional Go board
        """
        self.board = board
        self.rows = len(board)
        self.cols = 0 if self.rows == 0 else len(board[0])

    def onboard(self, x, y):
        """Check if a given coordinate is within the boundaries of the board.

        Args:
            x (int): Column index
            y (int): Row index

        Returns:
            bool: True if the coordinate is within the board boundaries, False otherwise.
        """
        return 0 <= x < self.cols and 0 <= y < self.rows

    def neighbors(self, x, y):
        """Find the neighboring coordinates of a given coordinate.

        Args:
            x (int): Column index
            y (int): Row index

        Returns:
            list: List of neighboring coordinates.
        """
        nbr = []
        for dx in (-1, 1):
            if self.onboard(x + dx, y):
                nbr.append((x + dx, y))
        for dy in (-1, 1):
            if self.onboard(x, y + dy):
                nbr.append((x, y + dy))
        return nbr
        
    def territory(self, x, y):
        """Find the owner and territories given a coordinate on the board.

        Args:
            x (int): Column index
            y (int): Row index

        Returns:
            tuple: A tuple containing the owner of the area ("W", "B", or ""), and a set of coordinates representing the owner's territories.
        """
        if not self.onboard(x, y):
            raise ValueError("Invalid coordinate")
        if self.board[y][x] != NONE:
            return NONE, set()
        owner = UNKNOWN
        visited = set()
        enclosed = set()
        stack = [(x, y)]
        while len(stack) != 0:
            c, r = stack.pop()
            visited.add((c, r))
            stone = self.board[r][c]
            if stone == NONE:
                enclosed.add((c, r))
                for n in self.neighbors(c, r):
                    if n not in visited:
                        stack.append(n)
            elif stone != owner:
                owner = stone if owner == UNKNOWN else NONE
        if owner == UNKNOWN:
            owner = NONE
        return owner, enclosed
            
    def territories(self):
        """Find the owners and territories of the entire board.

        Returns:
            dict: A dictionary containing the owners ("W", "B", or "") as keys, and sets of coordinates representing their territories as values.
        """
        territories = {WHITE: set(), BLACK: set(), NONE: set()}
        vacant = set((c, r) for c in range(self.cols) for r in range(self.rows) if self.board[r][c] == NONE)
        while len(vacant) != 0:
            v = vacant.pop()
            who, where = self.territory(v[0], v[1])
            vacant -= where
            territories[who] |= where
        return territories
