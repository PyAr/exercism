# Globals for the directions
# Change the values as needed
NORTH = [0, 1]
EAST = [1, 0]
SOUTH = [0, -1]
WEST = [-1, 0]

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        """
        Initialize the Robot with direction and coordinates.

        Args:
            direction (list, optional): Initial direction. Defaults to NORTH.
            x_pos (int, optional): Initial x-coordinate. Defaults to 0.
            y_pos (int, optional): Initial y-coordinate. Defaults to 0.
        """
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions):
        """
        Move the robot based on the provided instructions.

        Args:
            instructions (str): A string containing movement instructions ('R', 'L', 'A').
        """
        directions = [NORTH, EAST, SOUTH, WEST]
        for instruction in instructions:
            if instruction == "R":
                self.direction = directions[(directions.index(self.direction) + 1) % 4]
            elif instruction == "L":
                self.direction = directions[(directions.index(self.direction) - 1) % 4]
            elif instruction == "A":
                dx, dy = self.direction
                self.coordinates = (self.coordinates[0] + dx, self.coordinates[1] + dy)
