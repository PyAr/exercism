from typing import List

# Constants defining the animals and their associated phrases
ANIMAL_LINES = [
    ("fly", "I don't know why she swallowed the fly. Perhaps she'll die."),
    ("spider", "It wriggled and jiggled and tickled inside her."),
    ("bird", "How absurd to swallow a bird!"),
    ("cat", "Imagine that, to swallow a cat!"),
    ("dog", "What a hog, to swallow a dog!"),
    ("goat", "Just opened her throat and swallowed a goat!"),
    ("cow", "I don't know how she swallowed a cow!"),
    ("horse", "She's dead, of course!"),
]
SPIDER_LONG = "spider that wriggled and jiggled and tickled inside her"
FIRST_LINE = "I know an old lady who swallowed a "


def she_swallowed(curr_animal: str, prev_animal: str) -> str:
    """Constructs the line describing swallowing one animal to catch another."""
    return f"She swallowed the {curr_animal} to catch the {prev_animal}."


def recite(start_verse: int, end_verse: int) -> List[str]:
    """
    Generate verses of the song "I Know an Old Lady Who Swallowed a Fly" for the specified range.

    Args:
        start_verse (int): The starting verse number.
        end_verse (int): The ending verse number.

    Returns:
        List[str]: A list of strings containing the requested verses of the song, with empty strings between verses.
    """
    verses = {}  # Dictionary to store verses indexed by verse number
    cumulative_verse = []  # List to store lines of each verse
    prev_animal = ""  # Track the previous animal for constructing "swallowed" lines

    # Iterate over the ANIMAL_LINES to construct the verses
    for verse_num, line in enumerate(ANIMAL_LINES):
        curr_animal = line[0]
        animal_phrase = line[1]
        first_line = f"{FIRST_LINE}{curr_animal}."
        second_line = f"{animal_phrase}"

        # For the first verse, use the initial phrase and the animal's line
        if verse_num == 0:
            verses[verse_num] = [first_line, second_line]
            prev_animal = curr_animal
            cumulative_verse += [second_line]

        # For the second verse, add the phrase about the spider
        elif verse_num == 2:
            cumulative_verse = [she_swallowed(curr_animal, SPIDER_LONG)] + cumulative_verse
            verse = [first_line, second_line] + cumulative_verse
            verses[verse_num] = verse

        # For the last verse, use only the animal's line
        elif verse_num == 7:
            verses[verse_num] = [first_line, second_line]

        # For other verses, construct the "swallowed" line and add to the cumulative verse
        else:
            cumulative_verse = [she_swallowed(curr_animal, prev_animal)] + cumulative_verse
            verse = [first_line, second_line] + cumulative_verse
            verses[verse_num] = verse
        prev_animal = curr_animal

    # Recite the requested verses
    recited = []
    for verse_num in range(start_verse, end_verse + 1):
        recited += verses[verse_num - 1]
        if verse_num < end_verse:
            recited.append("")  # Add an empty string between verses
    return recited
