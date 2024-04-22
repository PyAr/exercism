class HighScores:
    """
    A class to represent a collection of high scores.

    ...

    Attributes
    ----------
    scores : list
        a list of integers representing the scores

    Methods
    -------
    latest():
        Returns the latest (last) score.
    personal_best():
        Returns the highest score.
    personal_top_three():
        Returns the three highest scores, sorted in descending order.
    """

    def __init__(self, scores):
        """
        Constructs all the necessary attributes for the HighScores object.

        Parameters
        ----------
            scores : list
                a list of integers representing the scores
        """
        self.scores = scores

    def latest(self):
        """
        Returns the latest (last) score.

        Returns
        -------
        int
            The latest score
        """
        return self.scores[-1]

    def personal_best(self):
        """
        Returns the highest score.

        Returns
        -------
        int
            The highest score
        """
        return max(self.scores)

    def personal_top_three(self):
        """
        Returns the three highest scores, sorted in descending order.

        Returns
        -------
        list
            The three highest scores
        """
        return sorted(self.scores, reverse=True)[:3]