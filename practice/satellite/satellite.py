class Node:
    """
    A class to represent a node in a binary tree.

    Attributes
    ----------
    value : int
        The value of the node.
    left : Node, optional
        The left child of the node (default is None).
    right : Node, optional
        The right child of the node (default is None).

    Methods
    -------
    to_dict():
        Converts the node and its children into a dictionary.
    """

    def __init__(self, value, left=None, right=None):
        """
        Constructs all the necessary attributes for the Node object.

        Parameters
        ----------
            value : int
                The value of the node.
            left : Node, optional
                The left child of the node (default is None).
            right : Node, optional
                The right child of the node (default is None).
        """
        self.value = value
        self.left = left
        self.right = right

    def to_dict(self):
        """
        Converts the node and its children into a dictionary.

        Returns
        -------
        dict
            A dictionary with keys 'v', 'l', 'r' representing value, left child, and right child respectively.
        """
        return {
            "v": self.value,
            "l": self.left.to_dict() if self.left else {},
            "r": self.right.to_dict() if self.right else {},
        }


def tree_from_traversals(preorder, inorder):
    """
    Constructs a binary tree from its preorder and inorder traversals.

    Parameters
    ----------
    preorder : list
        The preorder traversal of the tree.
    inorder : list
        The inorder traversal of the tree.

    Returns
    -------
    dict
        A dictionary representing the tree.

    Raises
    ------
    ValueError
        If the lengths of preorder and inorder are not the same,
        or if they do not contain the same elements,
        or if they do not contain unique items.
    """
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")

    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")

    if not preorder and not inorder:
        return {}

    root_value = preorder[0]
    root_index = inorder.index(root_value)

    left_subtree = tree_from_traversals(preorder[1:root_index+1], inorder[:root_index])
    right_subtree = tree_from_traversals(preorder[root_index+1:], inorder[root_index+1:])

    if isinstance(left_subtree, Node):
        left_subtree = left_subtree.to_dict()
    if isinstance(right_subtree, Node):
        right_subtree = right_subtree.to_dict()

    return {
        "v": root_value,
        "l": left_subtree,
        "r": right_subtree,
    }