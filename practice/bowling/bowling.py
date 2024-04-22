class Frame(object):
    """Represents a single frame in a bowling game."""

    def __init__(self, tenth=False):
        """
        Initialize a Frame.

        Args:
            tenth (bool): Indicates whether the frame is the tenth frame.
        """
        self.tenth = tenth
        self.pins = []

    def is_full(self):
        """Check if the frame is full."""
        if self.tenth:
            return len(self.pins) == 2 and sum(self.pins) < 10 or \
                   len(self.pins) == 3 and (sum(self.pins[:2]) == 10 or self.pins[0] == 10)
        else:
            return len(self.pins) == 2 or len(self.pins) == 1 and self.pins[0] == 10

    def is_invalid(self):
        """Check if the frame is invalid."""
        if self.tenth:
            return len(self.pins) == 2 and self.pins[0] < 10 and sum(self.pins) > 10 or \
                   len(self.pins) == 3 and self.pins[0] == 10 and self.pins[1] != 10 and sum(self.pins[1:]) > 10
        else:
            return sum(self.pins) > 10

    def roll(self, pins):
        """
        Add pins to the frame.

        Args:
            pins (int): The number of pins knocked down.

        Returns:
            bool: True if the frame is full after the roll, False otherwise.
        
        Raises:
            RuntimeError: If trying to add to a full frame.
            ValueError: If the frame becomes invalid after the roll.
        """
        if self.is_full():
            raise RuntimeError("Adding to full frame")
        else:
            self.pins.append(pins)
            if self.is_full() and self.is_invalid():
                raise ValueError("This frame is not valid: {}".format(self.pins))
            return self.is_full()

    def score(self, next_throws):
        """
        Calculate the score for the frame.

        Args:
            next_throws (list): The pins knocked down in the next throws.

        Returns:
            int: The score for the frame.
        """
        if next_throws:
            if self.pins[0] == 10:
                return sum(self.pins) + sum(next_throws[:2])
            elif sum(self.pins) == 10:
                return sum(self.pins) + next_throws[0]
            else:
                return sum(self.pins)
        else:
            return sum(self.pins)

    def __repr__(self):
        """Return a string representation of the Frame."""
        return "pins={}, full={}, is_invalid={}".format(self.pins, self.is_full(), self.is_invalid())

class BowlingGame(object):
    """Represents a bowling game."""

    def __init__(self):
        """Initialize a BowlingGame."""
        self.frames = [Frame() for _ in range(9)] + [Frame(tenth=True)]
        self.current = 0

    def is_full(self):
        """Check if the game is full."""
        return all([frame.is_full() for frame in self.frames])

    def roll(self, pins):
        """
        Roll the ball and add pins to the current frame.

        Args:
            pins (int): The number of pins knocked down.
        
        Raises:
            ValueError: If the pins value is invalid.
            IndexError: If trying to roll for a full game.
        """
        if not 0 <= pins <= 10:
            raise ValueError("Invalid pins value")
        elif self.is_full():
            raise IndexError("Trying to roll for full game")
        else:
            if self.frames[self.current].roll(pins):
                self.current += 1

    def score(self):
        """
        Calculate the final score of the game.

        Returns:
            int: The final score of the game.
        
        Raises:
            IndexError: If the game is incomplete.
        """
        if not self.is_full():
            raise IndexError("An incomplete game cannot be scored")

        score = 0
        for (i, frame) in enumerate(self.frames):
            next_throws = [throw for next_frame in self.frames[i+1:] for throw in next_frame.pins]
            score += frame.score(next_throws)

        return score
