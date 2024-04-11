def transform(legacy_data):
    transformed = {}
    for point, letters in legacy_data.items():
        for letter in letters:
            letter_lower = letter.lower()
            if letter_lower not in transformed:
                transformed[letter_lower] = point
    return transformed

