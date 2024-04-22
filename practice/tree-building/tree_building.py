""""
Build Tree - Build a tree structure from a list of records.

Approach:
1. Define a Record class to represent each record with attributes record_id and parent_id.
2. Define a Node class to represent each node in the tree with an ID and a list of children nodes.
3. Implement the BuildTree function to build a tree structure from a list of records.
4. Sort the records based on record_id to ensure they are in order.
5. Check if the record_ids are valid and in order, and if the parent_id of each node is smaller than its record_id.
6. Create a list of nodes corresponding to the records.
7. Iterate through the records to build the tree structure:
    - For each record, add its corresponding node to the children list of its parent node.
8. Return the root node of the tree.

Args:
    records (list): A list of Record objects representing records with record_id and parent_id.

Returns:
    Node or None: The root node of the built tree structure, or None if no records are provided.

Raises:
    ValueError: If record_id is invalid or out of order, if parent_id is not smaller than the record_id,
                or if a node other than the root has equal record and parent id.

Example:
    >>> records = [Record(0, 0), Record(1, 0), Record(2, 0)]
    >>> BuildTree(records)
    Node(node_id=0, children=[Node(node_id=1, children=[]), Node(node_id=2, children=[])])
"""

class Record:
    """Represents a record with attributes record_id and parent_id."""
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id

class Node:
    """Represents a node in the tree with an ID and a list of children nodes."""
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

def BuildTree(records):
    """
    Build a tree structure from a list of records.

    Args:
        records (list): A list of Record objects representing records with record_id and parent_id.

    Returns:
        Node or None: The root node of the built tree structure, or None if no records are provided.

    Raises:
        ValueError: If record_id is invalid or out of order, if parent_id is not smaller than the record_id,
                    or if a node other than the root has equal record and parent id.
    """
    root = None
    records.sort(key=lambda x: x.record_id)
    if records and records[-1].record_id != len(records) - 1:
        raise ValueError('Record id is invalid or out of order.')
    trees = [Node(records[i].record_id) for i in range(len(records))]
    for i in range(len(records)):
        if records[i].record_id < records[i].parent_id:
            raise ValueError('Node parent_id should be smaller than it\'s record_id.')
        if (records[i].record_id == records[i].parent_id and records[i].record_id != 0) or (records[i].record_id == 0 and records[i].parent_id != 0):
            raise ValueError('Only root should have equal record and parent id.')
        if records[i].record_id != 0:
            trees[records[i].parent_id].children.append(trees[i])
    if len(trees) > 0:
        root = trees[0]
    return root
