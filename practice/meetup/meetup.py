from datetime import date
import calendar


class MeetupDayException(Exception):
    """Custom exception for invalid meetup days."""
    
    def __init__(self, err, message="That day does not exist."):
        """Initialize the MeetupDayException."""
        self.err = err
        self.message = message
        super().__init__(self.message)


def meetup(year, month, number, weekday):
    """
    Calculate meetup days based on the provided year, month, number, and weekday.

    Args:
        year (int): The year.
        month (int): The month (1-12).
        number (str): The position of the meetup day ('first', 'second', 'third', 'fourth', 'fifth', 'teenth', 'last').
        weekday (str): The weekday ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday').

    Returns:
        date: The calculated meetup day.

    Raises:
        MeetupDayException: If the meetup day is not valid.
    """
    days_to_numbers = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    number_to_week = {'first': 0, 'second': 1, 'third': 2, 'fourth': 3, 'fifth': 4, 'last': -1}

    day_number = days_to_numbers[weekday]
    number = number.lower()

    if number == 'teenth':
        teenth_cal = calendar.Calendar()
        teenths = sorted(item for item in teenth_cal.itermonthdays4(year, month)
                         if 13 <= item[2] <= 19 and item[3] == day_number)

        if teenths:
            return date(*teenths[0][:3])
        else:
            raise MeetupDayException(f'Teenth not found for {weekday}')

    else:
        week_number = number_to_week[number]
        remaining_cal = calendar.Calendar()
        candidates = sorted(item for item in remaining_cal.itermonthdays4(year, month)
                            if item[1] == month and item[3] == day_number)

        try:
            return date(*candidates[week_number][:3])
        except (ValueError, IndexError) as err:
            raise MeetupDayException(err) from None
