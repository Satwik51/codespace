# Practical 10: Graph Representation and Traversals

## Practical Number
Practical 10

## Practical Title
Graph Representation and Traversals

## Problem Statement
Represent a graph using an adjacency-list representation and implement Breadth-First Search (BFS) and Depth-First Search (DFS). Use a Queue for BFS and recursion or an explicit Stack for DFS.

## Concepts Used
- Adjacency-list representation (`dict` mapping vertices to neighbor lists)
- Directed and Undirected graphs
- Breadth-First Search (BFS) using an explicit FIFO Queue
- Depth-First Search (DFS) using both recursion and an explicit LIFO Stack
- Handling cycles and disconnected graph components using a `visited` set

## Operations Implemented
- `add_vertex(v)` and `remove_vertex(v)`
- `add_edge(u, v)` and `remove_edge(u, v)`
- `display()` — Prints the adjacency list.
- `bfs(start)` and `bfs_all_components()`
- `dfs_recursive(start)`, `dfs_iterative(start)`, and `dfs_all_components()`

## How to Execute
```bash
cd "/home/satwik-rai/DS USING PYTHON LAB PRACTICALS/Lab_Practicals/Practical_10"
python3 main.py
```

## Sample Input and Output
```text
Undirected Graph:
Edges: (A, B), (A, C), (B, D), (C, E)
BFS Traversal (Queue)          from A: A -> B -> C -> D -> E
DFS Traversal (Recursive)      from A: A -> B -> D -> C -> E
DFS Traversal (Explicit Stack) from A: A -> B -> D -> C -> E
```

## Important Edge Cases Handled
- Empty graph and single-vertex graph with no edges.
- Cycles and self-loops (prevented from infinite looping via `visited` tracking).
- Duplicate edge additions ignored cleanly.
- Disconnected graphs (full traversal across all components supported).
- Non-existent start vertex, empty vertex labels, and invalid menu inputs.
