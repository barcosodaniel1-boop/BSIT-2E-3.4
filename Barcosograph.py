"""
Graph using the last name B A R C O S O
Traversals: BFS and DFS

The last name has two O's, so the vertices are named O1 and O2
internally and shown as "O" when printed.
"""
from collections import deque


def label(node):
    """Show O1 / O2 as plain 'O'."""
    return node[0]


# Adjacency list: each vertex maps to its neighbors (left to right).
graph = {
    "B":  ["A", "R", "C"],
    "A":  ["B", "O1", "S"],
    "R":  ["B", "S", "C"],
    "C":  ["B", "R", "O2"],
    "O1": ["A"],
    "S":  ["A", "R"],
    "O2": ["C"],
}


def graph_bfs(start):
    """BFS: visit all neighbors first, using a queue and a visited set."""
    visited, order, queue = {start}, [], deque([start])
    while queue:
        v = queue.popleft()
        order.append(v)
        for n in graph[v]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return order


def graph_dfs(v, visited=None, order=None):
    """DFS: go as deep as possible, then backtrack."""
    if visited is None:
        visited, order = set(), []
    visited.add(v)
    order.append(v)
    for n in graph[v]:
        if n not in visited:
            graph_dfs(n, visited, order)
    return order


def show(title, nodes):
    print(f"{title:<6}", " - ".join(label(n) for n in nodes))


if __name__ == "__main__":
    print("Last name: BARCOSO")
    print("GRAPH\n")
    show("BFS:", graph_bfs("B"))
    show("DFS:", graph_dfs("B"))