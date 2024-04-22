def commands(binary_str):
    """
    Decodes a binary string into a secret handshake.

    The binary string represents a sequence of actions, where each bit corresponds
    to an action from the list ['wink', 'double blink', 'close your eyes', 'jump'].
    If the first bit of the binary string is 1, the sequence of actions is reversed.

    Args:
        binary_str (str): The binary string to decode. It should contain up to 5 characters.

    Returns:
        list: The decoded sequence of actions.

    Raises:
        ValueError: If the binary string contains characters other than '0' and '1',
                    or if it is longer than 5 characters.

    Examples:
        >>> commands('101')
        ['close your eyes', 'wink']
    """
    if any(c not in '01' for c in binary_str) or len(binary_str) > 5:
        raise ValueError('Invalid binary string')

    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    handshake = []

    # Iterate over the bits in the binary string, in reverse order
    for i in range(4):
        # If the bit is '1', append the corresponding action to the handshake
        if binary_str[::-1][i:i+1] == '1':
            handshake.append(actions[i])

    # If the first bit of the binary string is '1', reverse the handshake
    if binary_str[0] == '1':
        handshake.reverse()

    return handshake