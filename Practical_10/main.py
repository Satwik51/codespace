"""
Practical 10: Graph Representation and Traversals
-------------------------------------------------
Represents a Graph (directed or undirected) using an adjacency list.
Implements Breadth-First Search (BFS) using an explicit Queue and
Depth-First Search (DFS) using both recursion and an explicit Stack.
"""


class SimpleQueue:
    """Explicit FIFO Queue implemented with linked nodes for BFS."""

    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        node = self._Node(item)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        val = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return val


class SimpleStack:
    """Explicit LIFO Stack for iterative DFS."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.items.pop()


class Graph:
    """Graph represented using an adjacency list."""

    def __init__(self, directed=False):
        self.directed = directed
        self.adj = {}

    def is_empty(self):
        return len(self.adj) == 0

    def add_vertex(self, vertex):
        """Add a vertex if not already present. Returns True if newly added."""
        if vertex in self.adj:
            return False
        self.adj[vertex] = []
        return True

    def add_edge(self, u, v):
        """
        Add edge u -> v (and v -> u if undirected).
        Automatically creates missing vertices and avoids duplicate edges.
        """
        self.add_vertex(u)
        self.add_vertex(v)

        if v not in self.adj[u]:
            self.adj[u].append(v)

        if not self.directed and u != v:
            if u not in self.adj[v]:
                self.adj[v].append(u)

    def remove_edge(self, u, v):
        """Remove edge u -> v (and v -> u if undirected). Returns True if removed."""
        if u not in self.adj or v not in self.adj:
            return False
        removed = False
        if v in self.adj[u]:
            self.adj[u].remove(v)
            removed = True
        if not self.directed and u != v and u in self.adj[v]:
            self.adj[v].remove(u)
            removed = True
        return removed

    def remove_vertex(self, vertex):
        """Remove a vertex and all edges pointing to it. Returns True if removed."""
        if vertex not in self.adj:
            return False
        del self.adj[vertex]
        for neighbors in self.adj.values():
            if vertex in neighbors:
                neighbors.remove(vertex)
        return True

    def display(self):
        if self.is_empty():
            print("Graph is empty (no vertices).")
            return
        gtype = "Directed" if self.directed else "Undirected"
        print(f"\nAdjacency List ({gtype} Graph, {len(self.adj)} vertices):")
        for vertex, neighbors in self.adj.items():
            print(f"  {vertex} -> {neighbors}")

    def bfs(self, start):
        """Breadth-First Search starting from 'start' using an explicit Queue."""
        if start not in self.adj:
            raise KeyError(f"Start vertex '{start}' does not exist in graph.")

        visited = set()
        order = []
        queue = SimpleQueue()

        visited.add(start)
        queue.enqueue(start)

        while not queue.is_empty():
            curr = queue.dequeue()
            order.append(curr)
            for neighbor in self.adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)

        return order

    def bfs_all_components(self):
        """Perform BFS across all vertices (covers disconnected components)."""
        if self.is_empty():
            return []
        visited = set()
        order = []
        queue = SimpleQueue()

        for start in self.adj:
            if start not in visited:
                visited.add(start)
                queue.enqueue(start)
                while not queue.is_empty():
                    curr = queue.dequeue()
                    order.append(curr)
                    for neighbor in self.adj[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.enqueue(neighbor)
        return order

    def dfs_recursive(self, start):
        """Depth-First Search starting from 'start' using recursion."""
        if start not in self.adj:
            raise KeyError(f"Start vertex '{start}' does not exist in graph.")

        visited = set()
        order = []
        self._dfs_helper(start, visited, order)
        return order

    def _dfs_helper(self, node, visited, order):
        visited.add(node)
        order.append(node)
        for neighbor in self.adj[node]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited, order)

    def dfs_iterative(self, start):
        """Depth-First Search starting from 'start' using an explicit Stack."""
        if start not in self.adj:
            raise KeyError(f"Start vertex '{start}' does not exist in graph.")

        visited = set()
        order = []
        stack = SimpleStack()
        stack.push(start)

        while not stack.is_empty():
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            order.append(curr)

            # Push neighbors in reverse order so left-most neighbor is visited first
            neighbors = self.adj[curr]
            i = len(neighbors) - 1
            while i >= 0:
                nbr = neighbors[i]
                if nbr not in visited:
                    stack.push(nbr)
                i -= 1

        return order

    def dfs_all_components(self):
        """Perform recursive DFS across all vertices (covers disconnected graphs)."""
        if self.is_empty():
            return []
        visited = set()
        order = []
        for start in self.adj:
            if start not in visited:
                self._dfs_helper(start, visited, order)
        return order


def read_int(prompt):
    """Safely read an integer from user input."""
    while True:
        raw = input(prompt).strip()
        if raw == "":
            print("Input cannot be empty. Please enter an integer.")
            continue
        try:
            return int(raw)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def read_vertex(prompt):
    """Read a non-empty vertex label."""
    while True:
        raw = input(prompt).strip()
        if raw == "":
            print("Vertex label cannot be empty.")
            continue
        return raw


def main():
    print("=== Practical 10: Graph Representation and Traversals ===")
    try:
        print("Select Graph Type:")
        print("1. Undirected Graph")
        print("2. Directed Graph")
        while True:
            g_choice = read_int("Enter choice (1 or 2): ")
            if g_choice in (1, 2):
                break
            print("Invalid choice. Please enter 1 or 2.")

        graph = Graph(directed=(g_choice == 2))

        while True:
            print("\n--- Menu ---")
            print("1. Add Vertex")
            print("2. Add Edge")
            print("3. Remove Edge")
            print("4. Remove Vertex")
            print("5. Display Adjacency List")
            print("6. Breadth-First Search (BFS) from Start Vertex (Queue)")
            print("7. Depth-First Search (DFS) from Start Vertex (Recursive & Stack)")
            print("8. Traverse Entire Graph (All Disconnected Components)")
            print("9. Exit")

            choice = read_int("Enter your choice (1-9): ")

            if choice == 1:
                v = read_vertex("Enter vertex label: ")
                if graph.add_vertex(v):
                    print(f"Added vertex '{v}'.")
                else:
                    print(f"Vertex '{v}' already exists.")

            elif choice == 2:
                u = read_vertex("Enter source vertex: ")
                v = read_vertex("Enter destination vertex: ")
                graph.add_edge(u, v)
                arrow = "->" if graph.directed else "<->"
                print(f"Added edge {u} {arrow} {v}.")

            elif choice == 3:
                if graph.is_empty():
                    print("Graph is empty.")
                else:
                    u = read_vertex("Enter source vertex: ")
                    v = read_vertex("Enter destination vertex: ")
                    if graph.remove_edge(u, v):
                        print(f"Removed edge between '{u}' and '{v}'.")
                    else:
                        print(f"Edge between '{u}' and '{v}' does not exist.")

            elif choice == 4:
                if graph.is_empty():
                    print("Graph is empty.")
                else:
                    v = read_vertex("Enter vertex to remove: ")
                    if graph.remove_vertex(v):
                        print(f"Removed vertex '{v}' and its incident edges.")
                    else:
                        print(f"Vertex '{v}' does not exist.")

            elif choice == 5:
                graph.display()

            elif choice == 6:
                if graph.is_empty():
                    print("Graph is empty. Add vertices first.")
                else:
                    start = read_vertex("Enter start vertex for BFS: ")
                    try:
                        order = graph.bfs(start)
                        print("BFS Traversal (Queue):", " -> ".join(order))
                    except KeyError as err:
                        print(f"Error: {err}")

            elif choice == 7:
                if graph.is_empty():
                    print("Graph is empty. Add vertices first.")
                else:
                    start = read_vertex("Enter start vertex for DFS: ")
                    try:
                        rec_order = graph.dfs_recursive(start)
                        iter_order = graph.dfs_iterative(start)
                        print("DFS Traversal (Recursive)     :", " -> ".join(rec_order))
                        print("DFS Traversal (Explicit Stack):", " -> ".join(iter_order))
                    except KeyError as err:
                        print(f"Error: {err}")

            elif choice == 8:
                if graph.is_empty():
                    print("Graph is empty.")
                else:
                    print("Full BFS (all components):", " -> ".join(graph.bfs_all_components()))
                    print("Full DFS (all components):", " -> ".join(graph.dfs_all_components()))

            elif choice == 9:
                print("Exiting Practical 10. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1 to 9.")

    except (EOFError, KeyboardInterrupt):
        print("\nProgram interrupted. Exiting cleanly.")


if __name__ == "__main__":
    main()
