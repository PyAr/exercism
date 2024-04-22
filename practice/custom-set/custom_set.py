class CustomSet:
    """Implements a custom set data structure."""

    def __init__(self, elements=[]):
        """
        Initialize CustomSet.

        Args:
            elements (list, optional): List of elements to initialize the set. Defaults to an empty list.
        """
        self.elements = set(elements)

    def isempty(self):
        """Check if the set is empty.

        Returns:
            bool: True if the set is empty, False otherwise.
        """
        return len(self.elements) == 0

    def __contains__(self, element):
        """
        Check if the set contains a specific element.

        Args:
            element: The element to check for membership.

        Returns:
            bool: True if the element is in the set, False otherwise.
        """
        return element in self.elements

    def issubset(self, other):
        """
        Check if the set is a subset of another set.

        Args:
            other (CustomSet): The other set to compare against.

        Returns:
            bool: True if the set is a subset of the other set, False otherwise.
        """
        return self.elements.issubset(other.elements)

    def isdisjoint(self, other):
        """
        Check if the set is disjoint from another set.

        Args:
            other (CustomSet): The other set to check for disjointness.

        Returns:
            bool: True if the set is disjoint from the other set, False otherwise.
        """
        return self.elements.isdisjoint(other.elements)

    def __eq__(self, other):
        """
        Check if two CustomSets are equal.

        Args:
            other (CustomSet): The other CustomSet to compare against.

        Returns:
            bool: True if the two sets are equal, False otherwise.
        """
        return self.elements == other.elements

    def add(self, element):
        """
        Add an element to the set.

        Args:
            element: The element to add to the set.
        """
        self.elements.add(element)

    def intersection(self, other):
        """
        Compute the intersection of two sets.

        Args:
            other (CustomSet): The other set to compute the intersection with.

        Returns:
            CustomSet: The intersection of the two sets.
        """
        return CustomSet(self.elements.intersection(other.elements))

    def __sub__(self, other):
        """
        Compute the set difference between two sets.

        Args:
            other (CustomSet): The other set to compute the difference with.

        Returns:
            CustomSet: The set difference.
        """
        return CustomSet(self.elements - other.elements)

    def __add__(self, other):
        """
        Compute the union of two sets.

        Args:
            other (CustomSet): The other set to compute the union with.

        Returns:
            CustomSet: The union of the two sets.
        """
        return CustomSet(self.elements.union(other.elements))
