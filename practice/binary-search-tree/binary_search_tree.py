class TreeNode:
    """Represents a single node in a binary search tree."""

    def __init__(self, data, left=None, right=None):
        """
        Initialize a TreeNode.

        Args:
            data: The data stored in the node.
            left (TreeNode): Reference to the left child node.
            right (TreeNode): Reference to the right child node.
        """
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """Return a string representation of the TreeNode."""
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    """Represents a binary search tree."""

    def __init__(self, tree_data):
        """
        Initialize a BinarySearchTree with a list of data elements.

        Args:
            tree_data (list): List of data elements to insert into the binary search tree.
        """
        self.root = None
        for data in tree_data:
            self.insert(data)

    def insert(self, data):
        """
        Insert a data element into the binary search tree.

        Args:
            data: The data element to insert.
        """
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        """
        Recursively insert a data element into the binary search tree.

        Args:
            data: The data element to insert.
            node (TreeNode): The current node being considered.
        """
        if data <= node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        """
        Search for a specific data element in the binary search tree.

        Args:
            data: The data element to search for.

        Returns:
            TreeNode: The node containing the data if found, otherwise None.
        """
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, node):
        """
        Recursively search for a specific data element in the binary search tree.

        Args:
            data: The data element to search for.
            node (TreeNode): The current node being considered.

        Returns:
            TreeNode: The node containing the data if found, otherwise None.
        """
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(data, node.left)
        else:
            return self._search_recursive(data, node.right)

    def data(self):
        """Get the root node of the binary search tree."""
        return self.root

    def sorted_data(self):
        """Get a list of data elements in sorted order."""
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        """
        Perform an inorder traversal of the binary search tree.

        Args:
            node (TreeNode): The current node being considered.

        Returns:
            list: A list of data elements in sorted order.
        """
        if node is None:
            return []
        return self._inorder_traversal(node.left) + [node.data] + self._inorder_traversal(node.right)
