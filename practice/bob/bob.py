def response(hey_bob):
    """
    Respond to a statement or question directed at 'Bob'.

    The function takes a string as input, representing something said to Bob.
    Bob's responses are based on the following rules:

    - Bob answers 'Sure.' if you ask him a question.
    - He answers 'Whoa, chill out!' if you yell at him (ALL CAPS).
    - He says 'Calm down, I know what I'm doing!' if you yell a question at him.
    - He says 'Fine. Be that way!' if you address him without actually saying anything.
    - He answers 'Whatever.' to anything else.

    Args:
        hey_bob (str): The statement or question directed at Bob.

    Returns:
        str: Bob's response.

    Examples:
        >>> response('Hello, Bob.')
        'Whatever.'
        >>> response('BOB!')
        'Whoa, chill out!'
    """
    # Remove trailing whitespace
    hey_bob = hey_bob.rstrip()

    # Check for an empty string
    if hey_bob == '':
        return "Fine. Be that way!"
    # Check for shouting (all uppercase)
    elif hey_bob.isupper():
        # Check for a shouted question
        if hey_bob.endswith('?'):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    # Check for a question
    elif hey_bob.endswith('?'):
        return "Sure."
    else:
        return "Whatever."