def is_isogram(string):
    """
    Check if the input string is an isogram.

    An isogram (also known as a "nonpattern word") is a word or phrase
    without a repeating letter, however spaces and hyphens are allowed
    to appear multiple times.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is an isogram, False otherwise.

    Examples:
        >>> is_isogram("subdermatoglyphic")
        True
        >>> is_isogram("Alphabet")
        False
    """
    # Remove hyphens and spaces, and convert to lowercase
    scrubbed = string.replace('-', '').replace(' ', '').lower()

    # An isogram has no repeating letters, so the length of the string
    # should be equal to the number of unique letters (the size of the set)
    return len(scrubbed) == len(set(scrubbed))