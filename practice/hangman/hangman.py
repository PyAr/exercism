# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    """
    A class representing a game of Hangman.

    Hangman is a guessing game where one player thinks of a word and the other
    tries to guess it by suggesting letters. The game ends when the word is
    fully guessed or the maximum number of incorrect guesses is reached.

    Attributes:
        word (str): The word to guess.
        remaining_guesses (int): The number of incorrect guesses remaining.
        status (str): The current status of the game ('win', 'lose', or 'ongoing').
        guessed_chars (set): The set of characters that have been guessed.
    """

    def __init__(self, word):
        """
        Initialize a new game of Hangman.

        Args:
            word (str): The word to guess.
        """
        self.word = word
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.guessed_chars = set()

    def guess(self, char):
        """
        Make a guess in the game.

        If the guessed character is in the word and has not been guessed before,
        it is added to the set of guessed characters. If it is not in the word
        or has been guessed before, the number of remaining guesses is decreased.

        The status of the game is updated after each guess.

        Args:
            char (str): The character to guess.

        Raises:
            ValueError: If the game has already ended.
        """
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        
        if char in self.guessed_chars:
            self.remaining_guesses -= 1
        else:
            self.guessed_chars.add(char)
            if char not in self.word:
                self.remaining_guesses -= 1
        
        if set(self.word) <= self.guessed_chars:
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        """
        Get the current state of the guessed word, with unguessed characters replaced by '_'.

        Returns:
            str: The guessed word with unguessed characters replaced by '_'.
        """
        return ''.join(c if c in self.guessed_chars else '_' for c in self.word)

    def get_status(self):
        """
        Get the current status of the game.

        Returns:
            str: The current status of the game ('win', 'lose', or 'ongoing').
        """
        return self.status