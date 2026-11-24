"""
Practical 07: Binary Trees and Binary Search Trees
--------------------------------------------------
Represents a Binary Tree using node objects, implements recursive Preorder,
Inorder, and Postorder traversals as well as Breadth-First (Level-Order)
traversal, and implements Binary Search Tree insertion, searching, and deletion.
"""


class TreeNode:
    """Node of a Binary Tree / Binary Search Tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class SimpleQueue:
    """Simple FIFO Queue using a linked list for Breadth-First Traversal."""

    class _QNode:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        node = self._QNode(value)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        val = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return val


class BinaryTree:
    """General Binary Tree with recursive DFS and BFS traversals."""

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert_level_order(self, data):
        """Insert a node in level-order (first available left/right slot)."""
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
            return

        queue = SimpleQueue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            curr = queue.dequeue()
            if curr.left is None:
                curr.left = new_node
                return
            queue.enqueue(curr.left)

            if curr.right is None:
                curr.right = new_node
                return
            queue.enqueue(curr.right)

    def insert_at_path(self, path, data):
        """
        Insert or replace a node using a path string of 'L' and 'R' from root.
        Empty path '' sets/updates the root node.
        """
        normalized = path.strip().upper()
        for ch in normalized:
            if ch not in ("L", "R"):
                raise ValueError("Path must contain only 'L' and 'R' characters.")

        if normalized == "":
            if self.root is None:
                self.root = TreeNode(data)
                return "Inserted root node."
            self.root.data = data
            return "Updated root node data."

        if self.root is None:
            raise ValueError("Tree has no root yet. Insert at empty path '' first.")

        curr = self.root
        for step in normalized[:-1]:
            if step == "L":
                if curr.left is None:
                    raise ValueError(
                        f"Missing intermediate left child along path '{normalized}'."
                    )
                curr = curr.left
            else:
                if curr.right is None:
                    raise ValueError(
                        f"Missing intermediate right child along path '{normalized}'."
                    )
                curr = curr.right

        last = normalized[-1]
        if last == "L":
            if curr.left is None:
                curr.left = TreeNode(data)
                return f"Inserted {data} as LEFT child at path '{normalized}'."
            curr.left.data = data
            return f"Updated LEFT child at path '{normalized}' to {data}."
        else:
            if curr.right is None:
                curr.right = TreeNode(data)
                return f"Inserted {data} as RIGHT child at path '{normalized}'."
            curr.right.data = data
            return f"Updated RIGHT child at path '{normalized}' to {data}."

    def preorder(self):
        result = []
        self._preorder_rec(self.root, result)
        return result

    def _preorder_rec(self, node, result):
        if node is None:
            return
        result.append(node.data)
        self._preorder_rec(node.left, result)
        self._preorder_rec(node.right, result)

    def inorder(self):
        result = []
        self._inorder_rec(self.root, result)
        return result

    def _inorder_rec(self, node, result):
        if node is None:
            return
        self._inorder_rec(node.left, result)
        result.append(node.data)
        self._inorder_rec(node.right, result)

    def postorder(self):
        result = []
        self._postorder_rec(self.root, result)
        return result

    def _postorder_rec(self, node, result):
        if node is None:
            return
        self._postorder_rec(node.left, result)
        self._postorder_rec(node.right, result)
        result.append(node.data)

    def breadth_first_traversal(self):
        """Return level-order traversal of the tree."""
        if self.root is None:
            return []
        result = []
        queue = SimpleQueue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            curr = queue.dequeue()
            result.append(curr.data)
            if curr.left is not None:
                queue.enqueue(curr.left)
            if curr.right is not None:
                queue.enqueue(curr.right)
        return result


class BinarySearchTree(BinaryTree):
    """Binary Search Tree supporting insertion, searching, and deletion."""

    def insert(self, data):
        """Insert data into BST. Returns True if inserted, False if duplicate."""
        if self.root is None:
            self.root = TreeNode(data)
            return True

        curr = self.root
        while True:
            if data == curr.data:
                return False
            if data < curr.data:
                if curr.left is None:
                    curr.left = TreeNode(data)
                    return True
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(data)
                    return True
                curr = curr.right

    def search(self, target):
        """Search target in BST. Returns (found: bool, comparisons: int)."""
        curr = self.root
        comparisons = 0
        while curr is not None:
            comparisons += 1
            if target == curr.data:
                return True, comparisons
            if target < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False, comparisons

    def delete(self, target):
        """Delete target from BST. Returns True if deleted, False if not found."""
        self.root, deleted = self._delete_rec(self.root, target)
        return deleted

    def _find_min_node(self, node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def _delete_rec(self, node, target):
        if node is None:
            return None, False

        if target < node.data:
            node.left, deleted = self._delete_rec(node.left, target)
            return node, deleted
        if target > node.data:
            node.right, deleted = self._delete_rec(node.right, target)
            return node, deleted

        # Found node to delete
        # Case 1 & Case 2: 0 or 1 child
        if node.left is None:
            return node.right, True
        if node.right is None:
            return node.left, True

        # Case 3: 2 children -> replace with inorder successor (min in right subtree)
        successor = self._find_min_node(node.right)
        node.data = successor.data
        node.right, _ = self._delete_rec(node.right, successor.data)
        return node, True


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


def show_traversals(tree, label):
    if tree.is_empty():
        print(f"{label} is empty.")
        return
    print(f"Preorder  (Root-Left-Right) : {tree.preorder()}")
    print(f"Inorder   (Left-Root-Right) : {tree.inorder()}")
    print(f"Postorder (Left-Right-Root) : {tree.postorder()}")
    print(f"Breadth-First (Level-Order) : {tree.breadth_first_traversal()}")


def binary_tree_menu(bt):
    while True:
        print("\n--- General Binary Tree Menu ---")
        print("1. Insert Node (Level-Order)")
        print("2. Insert / Update Node at Path (e.g. '', 'L', 'R', 'LR')")
        print("3. Preorder Traversal (Recursive)")
        print("4. Inorder Traversal (Recursive)")
        print("5. Postorder Traversal (Recursive)")
        print("6. Breadth-First Traversal (Level-Order)")
        print("7. Show All Traversals")
        print("8. Back to Main Menu")

        choice = read_int("Enter choice (1-8): ")
        if choice == 1:
            val = read_int("Enter integer value to insert: ")
            bt.insert_level_order(val)
            print(f"Inserted {val} in level-order.")
        elif choice == 2:
            path = input("Enter path from root ('' for root, e.g. 'L', 'LR'): ")
            val = read_int("Enter integer value: ")
            try:
                msg = bt.insert_at_path(path, val)
                print(msg)
            except ValueError as err:
                print(f"Error: {err}")
        elif choice == 3:
            print("Preorder :", bt.preorder())
        elif choice == 4:
            print("Inorder  :", bt.inorder())
        elif choice == 5:
            print("Postorder:", bt.postorder())
        elif choice == 6:
            print("BFS      :", bt.breadth_first_traversal())
        elif choice == 7:
            show_traversals(bt, "Binary Tree")
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please enter 1 to 8.")


def bst_menu(bst):
    while True:
        print("\n--- Binary Search Tree (BST) Menu ---")
        print("1. Insert Node")
        print("2. Search Node")
        print("3. Delete Node")
        print("4. Preorder Traversal")
        print("5. Inorder Traversal (Sorted Order)")
        print("6. Postorder Traversal")
        print("7. Breadth-First Traversal (Level-Order)")
        print("8. Show All Traversals")
        print("9. Back to Main Menu")

        choice = read_int("Enter choice (1-9): ")
        if choice == 1:
            val = read_int("Enter integer value to insert into BST: ")
            if bst.insert(val):
                print(f"Inserted {val} into BST.")
            else:
                print(f"Duplicate value {val} ignored (BST stores unique keys).")
        elif choice == 2:
            if bst.is_empty():
                print("BST is empty. Nothing to search.")
            else:
                target = read_int("Enter integer value to search: ")
                found, comps = bst.search(target)
                if found:
                    print(f"Found {target} in BST ({comps} comparison(s)).")
                else:
                    print(f"{target} not found in BST ({comps} comparison(s)).")
        elif choice == 3:
            if bst.is_empty():
                print("BST is empty. Nothing to delete.")
            else:
                target = read_int("Enter integer value to delete: ")
                if bst.delete(target):
                    print(f"Deleted {target} from BST.")
                else:
                    print(f"Value {target} not found in BST.")
        elif choice == 4:
            print("Preorder :", bst.preorder())
        elif choice == 5:
            print("Inorder  :", bst.inorder())
        elif choice == 6:
            print("Postorder:", bst.postorder())
        elif choice == 7:
            print("BFS      :", bst.breadth_first_traversal())
        elif choice == 8:
            show_traversals(bst, "BST")
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please enter 1 to 9.")


def main():
    print("=== Practical 07: Binary Trees and Binary Search Trees ===")
    bt = BinaryTree()
    bst = BinarySearchTree()

    try:
        while True:
            print("\n--- Main Menu ---")
            print("1. General Binary Tree Operations & Traversals")
            print("2. Binary Search Tree (BST) Operations & Traversals")
            print("3. Exit")

            choice = read_int("Enter your choice (1-3): ")
            if choice == 1:
                binary_tree_menu(bt)
            elif choice == 2:
                bst_menu(bst)
            elif choice == 3:
                print("Exiting Practical 07. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    except (EOFError, KeyboardInterrupt):
        print("\nProgram interrupted. Exiting cleanly.")


if __name__ == "__main__":
    main()
