"""
Assessment 3.6: DFS Methods in Tree
Binary tree built from the name D A N I E L  B A R C O S O
(letters are placed level by level, left to right)

Preorder:  Root -> Left -> Right
Inorder:   Left -> Root -> Right
Postorder: Left -> Right -> Root
"""


class Node:
    def __init__(self, letter):
        self.letter = letter
        self.left = None
        self.right = None


def build_tree(name):
    """Build a complete binary tree by inserting letters level by level."""
    letters = [ch for ch in name.upper() if ch.isalpha()]
    nodes = [Node(ch) for ch in letters]
    for i, node in enumerate(nodes):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0]


def preorder(node, result=None):
    """Root -> Left -> Right"""
    if result is None:
        result = []
    if node is not None:
        result.append(node.letter)
        preorder(node.left, result)
        preorder(node.right, result)
    return result


def inorder(node, result=None):
    """Left -> Root -> Right"""
    if result is None:
        result = []
    if node is not None:
        inorder(node.left, result)
        result.append(node.letter)
        inorder(node.right, result)
    return result


def postorder(node, result=None):
    """Left -> Right -> Root"""
    if result is None:
        result = []
    if node is not None:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.letter)
    return result


if __name__ == "__main__":
    root = build_tree("DANIEL BARCOSO")
    print("Name: DANIEL BARCOSO\n")
    print("Preorder :", " - ".join(preorder(root)))
    print("Inorder  :", " - ".join(inorder(root)))
    print("Postorder:", " - ".join(postorder(root)))