def build_tree(preorder_traversal, inorder_traversal):
    """Recursively constructs a binary tree.

    Args:
        preorder_traversal (list): Preorder traversal of the binary tree.
        inorder_traversal (list): Inorder traversal of the binary tree.

    Returns:
        dict: The constructed binary tree.
    """
    if len(preorder_traversal) == 0:
        return {}
    root_val = preorder_traversal.pop(0)
    root_index = inorder_traversal.index(root_val)
    inorder_traversal.pop(root_index)
    return {
        'v': root_val, 
        'l': build_tree(preorder_traversal[:root_index], inorder_traversal[:root_index]),
        'r': build_tree(preorder_traversal[root_index:], inorder_traversal[root_index:])}
        
    
def tree_from_traversals(preorder, inorder):
    """Constructs a binary tree from its preorder and inorder traversals.

    Args:
        preorder (list): Preorder traversal of the binary tree.
        inorder (list): Inorder traversal of the binary tree.

    Returns:
        dict: The constructed binary tree.
        
    Raises:
        ValueError: If traversals are invalid.
    """
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    if len(preorder) != len(set(preorder)):
        raise ValueError("traversals must contain unique items")
    return build_tree(preorder, inorder)
