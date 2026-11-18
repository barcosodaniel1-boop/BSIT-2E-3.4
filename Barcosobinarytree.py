"""
Binary Tree using the last name B A R C O S O
Traversals: BFS and DFS

The last name has two O's, so the nodes are named O1 and O2
internally and shown as "O" when printed.
"""
from collections import deque


def label(node):
    """Show O1 / O2 as plain 'O'."""
    return node[0]


# Each node maps to its [left, right] children.
tree = {
    "B": ["A", "R"],
    "A": ["C", "O1"],
    "R": ["S", "O2"],
    "C": [], "O1": [], "S": [], "O2": [],
}


def tree_bfs(root):
    """Breadth-First Search: visit level by level using a queue."""
    order, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        order.append(node)
        queue.extend(tree[node])          # left child, then right child
    return order


def tree_dfs(node, order=None):
    """Depth-First Search (preorder): root, left subtree, right subtree."""
    if order is None:
        order = []
    order.append(node)
    for child in tree[node]:
        tree_dfs(child, order)
    return order


def show(title, nodes):
    print(f"{title:<16}", " - ".join(label(n) for n in nodes))


if __name__ == "__main__":
    print("Last name: BARCOSO")
    print("BINARY TREE\n")
    show("BFS:", tree_bfs("B"))
    show("DFS (preorder):", tree_dfs("B"))