class Scale:
    NOTES = ["A", "AB", "B", "C", "CD", "D", "DE", "E", "F", "FG", "G", "GA"]
    SEL_SHARP = ["C", "a", "G", "D", "A", "E", "B", "e", "b"]
    
    def __init__(self, tonic):
        """Initialize the Scale object with the tonic note.

        Args:
            tonic (str): The tonic note for the scale.
        """
        self.tonic = tonic
 
    def chromatic(self):
        """Generate a chromatic scale based on the tonic note.

        Returns:
            list: A list of notes in the chromatic scale.
        """
        return self.interval()
 
    def interval(self, intervals="".join(["m" for note in NOTES[:-1]])):
        """Generate a scale based on specified intervals.

        Args:
            intervals (str, optional): String specifying intervals ('m' for minor, 'M' for major, 'A' for augmented). Defaults to "mmmmmmmmmmmm".

        Returns:
            list: A list of notes in the scale based on the specified intervals.
        """
        scale = self.get_scale(self.get_keysig())
        result = []
        result.append(self.tonic.capitalize())
        index = scale.index(self.tonic.capitalize())
        for interval in intervals:
            if interval == "m":
                index += 1
            if interval == "M":
                index += 2
            if interval == "A":
                index += 3
            index = index % len(scale)
            result.append(scale[index])
        return result
 
    def get_scale(self, keysig):
        """Determine the scale based on the key signature.

        Args:
            keysig (str): The key signature ("Sharp" or "Flat").

        Returns:
            list: A list of notes in the scale.
        """
        scale = []
        for note in self.NOTES:
            if len(note) == 1:
                scale.append(note)
            elif keysig == "Flat":
                scale.append("".join([note[1], "b"]))
            else:
                scale.append("".join([note[0], "#"]))
        return scale
 
    def get_keysig(self):
        """Determine the key signature based on the tonic note.

        Returns:
            str: The key signature ("Sharp" or "Flat").
        """
        if self.tonic in self.SEL_SHARP or self.tonic[-1] == "#":
            return "Sharp"
        return "Flat"
