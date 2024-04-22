import math
import string

def is_coprime(x, y):
    """
    Check if two numbers are coprime.

    Args:
        x (int): First number.
        y (int): Second number.

    Returns:
        bool: True if x and y are coprime, False otherwise.
    """
    return math.gcd(x, y) == 1

def encode(plain_text, a, b):
    """
    Encode plain text using the affine cipher.

    Args:
        plain_text (str): The plain text to be encoded.
        a (int): Coefficient 'a' for the affine cipher.
        b (int): Coefficient 'b' for the affine cipher.

    Returns:
        str: The encoded cipher text.
    
    Raises:
        ValueError: If 'a' and the length of the alphabet are not coprime.
    """
    alphabet = list(string.ascii_lowercase)
    numbers = list(string.digits)
    
    if not is_coprime(a, len(alphabet)):
        raise ValueError("a and m must be coprime.")
    
    indexes = []
    for letter in plain_text.lower():
        if letter in alphabet:
            indexes.append((a * alphabet.index(letter) + b) % len(alphabet))
        elif letter in numbers:
            indexes.append(int(letter) + 1000)
    
    out = ""
    for place, index in enumerate(indexes):
        if place % 5 == 0 and place > 1:
            out += " "
            if index < len(alphabet):
                out += alphabet[index]
            else:
                out += str(index - 1000)
        else:
            if index < len(alphabet):
                out += alphabet[index]
            else:
                out += str(index - 1000)
    
    return out

def decode(ciphered_text, a, b):
    """
    Decode ciphered text using the affine cipher.

    Args:
        ciphered_text (str): The ciphered text to be decoded.
        a (int): Coefficient 'a' for the affine cipher.
        b (int): Coefficient 'b' for the affine cipher.

    Returns:
        str: The decoded plain text.
    
    Raises:
        ValueError: If 'a' and the length of the alphabet are not coprime.
    """
    alphabet = list(string.ascii_lowercase)
    numbers = list(string.digits)
    
    if not is_coprime(a, len(alphabet)):
        raise ValueError("a and m must be coprime.")
    
    indexes = []
    for letter in ciphered_text:
        if letter in numbers:
            indexes.append(int(letter) + 1000)
        elif letter in alphabet:
            indexes.append(
                pow(a, -1, len(alphabet)) * (alphabet.index(letter) - b) % len(alphabet)
            )
    
    return "".join(
        [
            str(letter - 1000) if letter > len(alphabet) else alphabet[letter]
            for letter in indexes
        ]
    )
