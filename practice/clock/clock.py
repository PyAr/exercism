class Clock:
    """
    A class to represent a 24-hour clock.

    ...

    Attributes
    ----------
    minutes : int
        the total minutes past midnight

    Methods
    -------
    __repr__():
        Returns a string representation of the clock.
    __str__():
        Returns a string representation of the clock in HH:MM format.
    __eq__(other):
        Checks if this clock is equal to another clock.
    __add__(minutes):
        Adds a certain number of minutes to this clock.
    __sub__(minutes):
        Subtracts a certain number of minutes from this clock.
    """

    def __init__(self, hour, minute):
        """
        Constructs all the necessary attributes for the clock object.

        Parameters
        ----------
            hour : int
                the hour of the day
            minute : int
                the minute of the hour
        """
        self.minutes = (hour * 60 + minute) % 1440

    def __repr__(self):
        """
        Returns a string representation of the clock.

        Returns
        -------
        str
            a string representation of the clock
        """
        return f"Clock({self.minutes // 60}, {self.minutes % 60})"

    def __str__(self):
        """
        Returns a string representation of the clock in HH:MM format.

        Returns
        -------
        str
            a string representation of the clock in HH:MM format
        """
        return f"{self.minutes // 60:02d}:{self.minutes % 60:02d}"

    def __eq__(self, other):
        """
        Checks if this clock is equal to another clock.

        Parameters
        ----------
            other : Clock
                the other clock to compare with

        Returns
        -------
        bool
            True if the clocks are equal, False otherwise
        """
        return self.minutes == other.minutes

    def __add__(self, minutes):
        """
        Adds a certain number of minutes to this clock.

        Parameters
        ----------
            minutes : int
                the number of minutes to add

        Returns
        -------
        Clock
            a new clock with the added minutes
        """
        total_minutes = self.minutes + minutes
        return Clock(total_minutes // 60, total_minutes % 60)

    def __sub__(self, minutes):
        """
        Subtracts a certain number of minutes from this clock.

        Parameters
        ----------
            minutes : int
                the number of minutes to subtract

        Returns
        -------
        Clock
            a new clock with the subtracted minutes
        """
        total_minutes = self.minutes - minutes
        return Clock(total_minutes // 60, total_minutes % 60)