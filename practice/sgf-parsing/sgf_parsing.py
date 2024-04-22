''' Approach:
The provided code defines a class `SgfTree` to represent a tree structure with properties and children, and a function `parse` to parse SGF (Smart Game Format) strings into tree structures.
The `SgfTree` class has methods for equality comparison, representation, and inequality comparison.
The `parse` function takes an SGF string as input and constructs an `SgfTree` object representing the parsed tree structure.
The parsing process involves handling property-value pairs, nested tree structures, and handling escape characters.
The function iterates through the input string, extracting property-value pairs and recursively parsing nested tree structures.
The code utilizes regular expressions to extract property-value pairs and handle escape characters efficiently.
'''

import re

class SgfTree:
    """Represent a tree structure with properties and children."""

    def __init__(self, properties=None, children=None):
        """
        Initialize an SgfTree object with properties and children.

        Args:
            properties (dict, optional): Dictionary of properties. Defaults to None.
            children (list, optional): List of child SgfTree objects. Defaults to None.
        """
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        """Check if two SgfTree objects are equal."""
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __repr__(self):
        """Return a string representation of the SgfTree object."""
        return f"SgfTree(properties={self.properties!r}, children={self.children!r})"

    def __ne__(self, other):
        """Check if two SgfTree objects are not equal."""
        return not self == other

def parse(input_string):
    """Parse an SGF string into an SgfTree object."""
    if input_string == "(;)":
        return SgfTree()
    if not input_string.startswith("("):
        raise ValueError("tree missing")
    prop_val_regex = r"\[(?:\\.|[^\]])+\]"
    prop_regex = r"[A-Za-z]+(?:" + prop_val_regex + ")*"
    m = re.search(r"^\(;((?:" + prop_regex + ")+)(.*)\)$", input_string)
    if not m:
        raise ValueError("tree with no nodes")
    props, children = m[1], m[2]
    properties = {}
    for prop in re.findall(prop_regex, props):
        name = prop.split("[")[0]
        vals = [
            re.sub(r"\\(.)", r"\1", x[1:-1].replace("\t", " ")).replace("\\\n", "")
            for x in re.findall(prop_val_regex, prop)
        ]
        if not vals:
            raise ValueError("properties without delimiter")
        if not name.isupper():
            raise ValueError("property must be in uppercase")
        properties[name] = vals
    if children.startswith(";"):
        children = f"({children})"
    child_list = []
    curr_child = ""
    depth = 0
    for c in children:
        curr_child += c
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth < 0:
                raise ValueError("unbalanced parentheses")
            if depth == 0:
                child_list.append(curr_child)
                curr_child = ""
    return SgfTree(properties=properties, children=list(map(parse, child_list)))
