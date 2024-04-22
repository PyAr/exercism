def process_section(section, digits):
    """
    Process a section of the input grid and convert it to a string of digits.

    Args:
        section (list): A list of strings representing a section of the input grid.
        digits (dict): A dictionary mapping grid patterns to digits.

    Returns:
        str: A string of digits representing the section.

    Examples:
        >>> process_section([" _ ", "| |", "|_|", "   "], digits)
        '0'
    """
    # Create chunks by joining every three characters in each row of the section
    chunks = [''.join(row[i:i+3] for row in section) for i in range(0, len(section[0]), 3)]
    
    # Convert each chunk to a digit (or '?' if the chunk is not recognized)
    output = [digits.get(chunk, '?') for chunk in chunks]
    
    # Join the digits into a string and return it
    return ''.join(output)


def convert(input_grid):
    """
    Convert an OCR number grid to a string of digits.

    Args:
        input_grid (list): A list of strings representing the OCR number grid.

    Returns:
        str: A string of digits representing the OCR number grid.

    Raises:
        ValueError: If the number of input lines is not a multiple of four or
                    if the number of input columns is not a multiple of three.

    Examples:
        >>> convert([" _ ", "| |", "|_|", "   ", "    ", "  |", "  |", "   "])
        '0,1'
    """
    # Define the mapping from grid patterns to digits
    digits = {
        " _ | ||_|   ": "0",
        "     |  |   ": "1",
        " _  _||_    ": "2",
        " _  _| _|   ": "3",
        "   |_|  |   ": "4",
        " _ |_  _|   ": "5",
        " _ |_ |_|   ": "6",
        " _   |  |   ": "7",
        " _ |_||_|   ": "8",
        " _ |_| _|   ": "9",
    }

    # Check if the number of input lines is a multiple of four
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    
    # Check if the number of input columns is a multiple of three
    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    # Split the input grid into sections
    sections = [input_grid[i:i+4] for i in range(0, len(input_grid), 4)]
    
    # Process each section and join the results with commas
    return ','.join(process_section(section, digits) for section in sections)