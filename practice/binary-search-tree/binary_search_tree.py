class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data  # Data stored in the node
        self.left = left  # Reference to the left child node
        self.right = right  # Reference to the right child node

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None  # Root node of the binary search tree
        for data in tree_data:
            self.insert(data)  # Insert each data element into the binary search tree

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)  # If the tree is empty, create a new root node
        else:
            self._insert_recursive(data, self.root)  # Otherwise, insert the data recursively

    def _insert_recursive(self, data, node):
        if data <= node.data:
            if node.left is None:
                node.left = TreeNode(data)  # If the left child is None, create a new node
            else:
                self._insert_recursive(data, node.left)  # Otherwise, insert the data recursively in the left subtree
        else:
            if node.right is None:
                node.right = TreeNode(data)  # If the right child is None, create a new node
            else:
                self._insert_recursive(data, node.right)  # Otherwise, insert the data recursively in the right subtree

    def search(self, data):
        return self._search_recursive(data, self.root)  # Search for a data element in the binary search tree

    def _search_recursive(self, data, node):
        if node is None or node.data == data:
            return node  # If the node is None or the data matches, return the node
        if data < node.data:
            return self._search_recursive(data, node.left)  # If the data is less than the node's data, search in the left subtree
        else:
            return self._search_recursive(data, node.right)  # Otherwise, search in the right subtree

    def data(self):
        return self.root  # Return the root node of the binary search tree

    def sorted_data(self):
        return self._inorder_traversal(self.root)  # Perform inorder traversal to get the sorted data

    def _inorder_traversal(self, node):
        if node is None:
            return []  # If the node is None, return an empty list
        return self._inorder_traversal(node.left) + [node.data] + self._inorder_traversal(node.right)  # Perform inorder traversal recursively and concatenate the results
