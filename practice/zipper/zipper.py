class Zipper:
    @staticmethod
    def from_tree(tree):
        """
        Constructs a Zipper instance from a given tree.

        Args:
            tree (dict): The tree to construct the Zipper instance from.

        Returns:
            Zipper: The constructed Zipper instance.
        """
        return Zipper(dict(tree), [])

    def __init__(self, tree, ancestors):
        """
        Initializes a Zipper instance with a tree and ancestors.

        Args:
            tree (dict): The tree associated with the Zipper instance.
            ancestors (list): The list of ancestors of the current node in the tree.
        """
        self.tree = tree
        self.ancestors = ancestors

    def value(self):
        """
        Returns the value of the current node.

        Returns:
            Any: The value of the current node.
        """
        return self.tree['value']

    def set_value(self, value):
        """
        Sets the value of the current node.

        Args:
            value (Any): The value to set for the current node.

        Returns:
            Zipper: The updated Zipper instance.
        """
        self.tree['value'] = value
        return self

    def left(self):
        """
        Moves to the left child node if it exists.

        Returns:
            Zipper or None: The Zipper instance representing the left child node,
                or None if the left child node does not exist.
        """
        if self.tree['left'] is None:
            return None
        return Zipper(self.tree['left'], self.ancestors + [self.tree])

    def set_left(self, tree):
        """
        Sets the left child of the current node.

        Args:
            tree (dict): The tree to set as the left child of the current node.

        Returns:
            Zipper: The updated Zipper instance.
        """
        self.tree['left'] = tree
        return self

    def right(self):
        """
        Moves to the right child node if it exists.

        Returns:
            Zipper or None: The Zipper instance representing the right child node,
                or None if the right child node does not exist.
        """
        if self.tree['right'] is None:
            return None
        return Zipper(self.tree['right'], self.ancestors + [self.tree])

    def set_right(self, tree):
        """
        Sets the right child of the current node.

        Args:
            tree (dict): The tree to set as the right child of the current node.

        Returns:
            Zipper: The updated Zipper instance.
        """
        self.tree['right'] = tree
        return self

    def up(self):
        """
        Moves to the parent node if it exists.

        Returns:
            Zipper or None: The Zipper instance representing the parent node,
                or None if the parent node does not exist.
        """
        if not self.ancestors:
            return None
        return Zipper(self.ancestors[-1], self.ancestors[:-1])

    def to_tree(self):
        """
        Returns the root of the tree.

        Returns:
            dict: The root of the tree associated with the Zipper instance.
        """
        if any(self.ancestors):
            return self.ancestors[0]
        return self.tree
