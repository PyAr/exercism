from itertools import permutations
from typing import Dict, Optional, List, Tuple


def parse_puzzle(puzzle: str) -> Tuple[List[str], str]:
    """
    Parse the alphametics puzzle into a list of words and the result.

    Args:
        puzzle (str): The alphametics puzzle to parse.

    Returns:
        Tuple[List[str], str]: A tuple containing a list of words and the result.
    """
    # Split the puzzle into words and the result
    inputs, value = puzzle.split(" == ")
    # Split the words based on the '+' sign and strip whitespace
    words = [i.strip() for i in inputs.split("+")]
    return (words, value.strip())


def solve(puzzle: str) -> Optional[Dict[str, int]]:
    """
    Solve an alphametics puzzle.

    Args:
        puzzle (str): The alphametics puzzle to solve.

    Returns:
        Optional[Dict[str, int]]: A dictionary mapping characters to digits if a solution is found,
                                  otherwise None.
    """
    # Parse the puzzle into words and the result
    words, value = parse_puzzle(puzzle)
    # Find the first character of each word and the result
    nonzero = set([w[0] for w in words + [value] if len(w) > 1])
    # Gather all unique letters in the puzzle
    letters = list(set("".join(words + [value])) - nonzero) + list(nonzero)
    
    # Iterate through all permutations of digits
    for perm in permutations("0123456789", len(letters)):
        conv_dict = dict(zip(letters, perm))
        # Skip permutations where leading letters map to '0'
        if "0" in perm[-len(nonzero):]:
            continue

        # Convert words to integers based on the permutation
        values = [int("".join(conv_dict[w] for w in word)) for word in words]
        # Convert the result to an integer based on the permutation
        summed = int("".join(conv_dict[v] for v in value))

        # Check if the sum of the words equals the result
        if sum(values) == summed:
            return {k: int(v) for k, v in conv_dict.items()}
    return None
