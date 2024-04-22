def rows(row_count):
    """
    Generate the first `row_count` rows of Pascal's Triangle.

    Pascal's Triangle is a triangle of numbers where each number is the sum of
    the two numbers directly above it. The triangle starts with a single 1 at
    the top, and each row has one more element than the previous row.

    Args:
        row_count (int): The number of rows to generate.

    Returns:
        list: A list of lists representing the first `row_count` rows of Pascal's Triangle.

    Raises:
        ValueError: If `row_count` is negative.

    Examples:
        >>> rows(3)
        [[1], [1, 1], [1, 2, 1]]
    """
    if row_count < 0:
        raise ValueError("number of rows is negative")
    elif row_count == 0:
        return []
    elif row_count == 1:
        return [[1]]
    else:
        # Generate the first `row_count - 1` rows
        triangle = rows(row_count - 1)

        # Calculate the new row based on the last row
        last_row = triangle[-1]
        new_row = [1] + [last_row[i] + last_row[i+1] for i in range(len(last_row) - 1)] + [1]

        # Append the new row to the triangle and return it
        triangle.append(new_row)
        return triangle