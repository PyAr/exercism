def transform(old_dict):
    """
    Transforms the input dictionary by swapping keys with values.

    The function iterates over each key-value pair in the input dictionary.
    Each value is expected to be a list. For each element in the list, a new
    key-value pair is added to the output dictionary, where the key is the
    element (converted to lowercase) and the value is the original key from
    the input dictionary.

    Args:
        old_dict (dict): A dictionary to be transformed. Each value should be
            a list.

    Returns:
        dict: The transformed dictionary.

    Raises:
        TypeError: If a value in the input dictionary is not a list.
    """
    new_dict = {}
    for point, letters in old_dict.items():
        if not isinstance(letters, list):
            raise TypeError('Each value in the input dictionary should be a list.')
        for letter in letters:
            # Convert the letter to lowercase and add it to the new dictionary
            new_dict[letter.lower()] = point
    return new_dict