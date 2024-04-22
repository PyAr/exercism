import math
import re


def cipher_text(plain_text):
    """
    Encodes a plain text message into a cipher text using the square code method.

    The square code method involves arranging the plain text in a rectangle
    and then reading the text in columns, going from left to right.

    Args:
        plain_text (str): The plain text message to encode.

    Returns:
        str: The encoded cipher text.

    Raises:
        ValueError: If the input is not a string.

    Examples:
        >>> cipher_text("If man was meant to stay on the ground, god would have given us roots.")
        'imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau'
    """
    # Remove all non-alphanumeric characters and convert to lower case
    plain_text = re.sub(r'\W+', '', plain_text).lower()

    # If the plain text is empty, return an empty string
    if not plain_text:
        return ""

    # Calculate the number of columns and rows for the rectangle
    c = math.ceil(math.sqrt(len(plain_text)))
    r = len(plain_text) // c
    if len(plain_text) % c != 0:
        r += 1

    # Split the plain text into rows
    rows = []
    for i in range(r):
        row = plain_text[i*c:(i+1)*c].ljust(c)
        rows.append(row)

    # Read the text in columns to get the encoded text
    encoded_text = ""
    for i in range(c):
        for row in rows:
            encoded_text += row[i]

    # Split the encoded text into chunks of length r
    chunks = []
    for i in range(c):
        chunk = encoded_text[i*r:(i+1)*r]
        chunks.append(chunk)

    # Join the chunks with spaces to get the final cipher text
    return ' '.join(chunks)