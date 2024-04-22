from json import dumps


class Tree:
    """A class representing a tree and its operations."""

    def __init__(self, label, children=None):
        """
        Initialize a Tree object with a label and optional children.

        Args:
            label (any): The label of the tree node.
            children (list, optional): List of child Tree objects. Defaults to None.
        """
        self.label = label
        self.children = children if children is not None else []

    def to_dict(self):
        """
        Convert the tree to a dictionary representation.

        Returns:
            dict: Dictionary representation of the tree.
        """
        return {self.label: [c.to_dict() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        """
        Convert the tree to a JSON-formatted string.

        Args:
            indent (int, optional): Indentation level. Defaults to None.

        Returns:
            str: JSON-formatted string representing the tree.
        """
        return dumps(self.to_dict(), indent=indent)

    def __lt__(self, other):
        """
        Compare two Tree objects based on their labels.

        Args:
            other (Tree): Another Tree object.

        Returns:
            bool: True if the current object's label is less than the other object's label, False otherwise.
        """
        return self.label < other.label

    def __eq__(self, other):
        """
        Compare two Tree objects for equality.

        Args:
            other (Tree): Another Tree object.

        Returns:
            bool: True if the two objects are equal, False otherwise.
        """
        return self.to_dict() == other.to_dict()

    def from_pov(self, from_node):
        """
        Reorient the tree from the perspective of a specific node.

        Args:
            from_node (any): The label of the node from which the tree should be reoriented.

        Returns:
            Tree: The reoriented tree.

        Raises:
            ValueError: If the specified node is not found in the tree.
        """
        cur_path = [[self, 0]]
        while cur_path:
            subtree, next_index = cur_path[-1]
            if subtree.label == from_node:
                break
            if next_index < len(subtree.children):
                next_node = subtree.children[next_index]
                cur_path[-1][1] += 1
                cur_path.append([next_node, 0])
            else:
                cur_path.pop()
        if not cur_path:
            raise ValueError("Tree could not be reoriented")
        it = iter(cur_path)
        p = next(it)
        for c in it:
            p[0].children.pop(p[1] - 1)
            c[0].children.append(p[0])
            p = c
        return cur_path[-1][0]

    def path_to(self, from_node, to_node):
        """
        Find the path between two nodes in the tree.

        Args:
            from_node (any): The label of the starting node.
            to_node (any): The label of the target node.

        Returns:
            list: The path from the starting node to the target node.

        Raises:
            ValueError: If the starting node is not found in the tree or if no path is found between the two nodes.
        """
        to_find = {from_node, to_node}
        found_paths = dict()
        cur_path = []

        def helper(subtree):
            nonlocal to_find, found_paths, cur_path
            cur_path.append(subtree.label)
            if subtree.label in to_find:
                found_paths[subtree.label] = cur_path.copy()
                to_find.remove(subtree.label)
            for c in subtree.children:
                if len(to_find) == 0:
                    break
                helper(c)
            cur_path.pop()

        helper(self)
        if from_node in to_find:
            raise ValueError("Tree could not be reoriented")
        if to_node in to_find:
            raise ValueError("No path found")

        from_path = found_paths[from_node]
        to_path = found_paths[to_node]
        from_part = []
        to_part = []

        while len(from_path) > len(to_path):
            from_part.append(from_path.pop())
        while len(to_path) > len(from_path):
            to_part.append(to_path.pop())
        while from_path[-1] != to_path[-1]:
            from_part.append(from_path.pop())
            to_part.append(to_path.pop())
        from_part.append(from_path[-1])
        to_part.reverse()
        from_part.extend(to_part)
        return from_part
