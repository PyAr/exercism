from itertools import permutations

def solve():
    """
    Iterate through all possible permutations of attributes for each house, 
    applying the given constraints and return the solution when found.

    Returns:
        list: A list containing dictionaries with solutions for each attribute.
            Each dictionary represents a house with its attributes.
            Example: [{'person': 'Norwegian', 'color': 'yellow', 'drink': 'water', 'animal': 'fox', 'smoke': 'Chesterfields'}, ...]

    """
    people = ("Norwegian", "Englishman", "Spaniard", "Ukrainian", "Japanese")
    colors = ("green", "blue", "red", "yellow", "ivory")
    animals = ("dog", "snails", "horse", "fox", "zebra")
    drinks = ("tea", "milk", "coffee", "orange juice", "water")
    smokes = ("Old Gold", "Chesterfields", "Kools", "Lucky Strike", "Parliaments")

    peoplemix = [x for x in permutations(people) if x[0] == "Norwegian" and x[2] == "Englishman" and x[1] != "Spaniard"]
    colormix = [x for x in permutations(colors) if x[1] == "blue" and x.index("ivory") - x.index("green") == 1 and x[0] != "red" and x[2] != "green"]
    drinkmix = [x for x in permutations(drinks) if x[2] == "milk" and x[3] == "coffee" and "tea" not in (x[0], x[2]) and x[0] != "orange juice"]
    animalmix = [x for x in permutations(animals) if x[0] != "dog" and x[1] == "horse"]
    smokemix = [x for x in permutations(smokes) if x[0] == "Kools" and "Lucky Strike" not in (x[2], x[3]) and x[1] != "Old Gold"]
    
    for p in peoplemix:
        for c in colormix:
            for d in drinkmix:
                for a in animalmix:
                    for s in smokemix:
                        if p.index("Ukrainian") == d.index("tea") and p.index("Spaniard") == a.index("dog") and abs(s.index("Chesterfields") - a.index("fox")) == 1 and s.index("Old Gold") == a.index("snails") and s.index("Lucky Strike") == d.index("orange juice") and p.index("Japanese") == s.index("Parliaments"):
                            return [{'person': p[i], 'color': c[i], 'drink': d[i], 'animal': a[i], 'smoke': s[i]} for i in range(5)]

solution = solve()

def drinks_water():
    """
    Returns the person who drinks water.

    Returns:
        str: The name of the person who drinks water.

    """
    for t in solution:
        if t['drink'] == 'water':
            return t['person']

def owns_zebra():
    """
    Returns the person who owns the zebra.

    Returns:
        str: The name of the person who owns the zebra.

    """
    for t in solution:
        if t['animal'] == 'zebra':
            return t['person']

class TreeNode:
    """
    Represents a node in a binary search tree.

    Attributes:
        data: The data stored in the node.
        left: The left child of the node.
        right: The right child of the node.
    """

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    """
    Represents a binary search tree.

    Attributes:
        root: The root node of the binary search tree.
    """

    def __init__(self, tree_data):
        """
        Initialize the binary search tree with data.

        Args:
            tree_data (list): A list of data items to initialize the tree.
        """
        self.root = None
        for data in tree_data:
            self.add(data)

    def add(self, data):
        """
        Inserts new data item into the binary search tree while maintaining the sorted order.

        Args:
            data: The data item to be inserted.
        """
        if self.root is None:
            self.root = TreeNode(data)
            return
        inserted = False
        cur_node = self.root

        while not inserted:
            if data <= cur_node.data:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = TreeNode(data)
                    inserted = True
            elif data > cur_node.data:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = TreeNode(data)
                    inserted = True

    def _inorder_traverse(self, node, elements):
        if node is not None:
            self._inorder_traverse(node.left, elements)
            elements.append(node.data)
            self._inorder_traverse(node.right, elements)

    def data(self):
        """
        Returns the root node of the binary search tree.

        Returns:
            TreeNode: The root node of the binary search tree.
        """
        return self.root

    def sorted_data(self):
        """
        Performs in-order traversal of the tree to retrieve all data items in sorted order.

        Returns:
            list: A list of data items in sorted order.
        """
        elements = []
        self._inorder_traverse(self.root, elements)
        return elements
