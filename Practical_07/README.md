# Practical 07: Binary Trees and Binary Search Trees

## Practical Number
Practical 07

## Practical Title
Binary Trees and Binary Search Trees

## Problem Statement
Represent a Binary Tree using node objects. Implement recursive preorder, inorder, and postorder traversals and breadth-first traversal. Implement Binary Search Tree operations for insertion, searching, and deletion.

## Concepts Used
- Binary Tree node representation (`data`, `left`, `right`)
- Recursive Depth-First Traversals (Preorder, Inorder, Postorder)
- Breadth-First (Level-Order) Traversal using an explicit FIFO Queue
- Binary Search Tree (BST) invariant (`left < root < right`)
- BST Deletion cases: leaf node, 1-child node, and 2-children node (using inorder successor)

## Operations Implemented
- **BinaryTree**: `insert_level_order`, `insert_at_path`, `preorder`, `inorder`, `postorder`, `breadth_first_traversal`
- **BinarySearchTree**: `insert`, `search`, `delete`, plus all four traversals

## How to Execute
```bash
cd "/home/satwik-rai/DS USING PYTHON LAB PRACTICALS/Lab_Practicals/Practical_07"
python3 main.py
```

## Sample Input and Output
```text
BST Insert: 50, 30, 70, 20, 40, 60, 80
Inorder   (Left-Root-Right) : [20, 30, 40, 50, 60, 70, 80]
Preorder  (Root-Left-Right) : [50, 30, 20, 40, 70, 60, 80]
Postorder (Left-Right-Root) : [20, 40, 30, 60, 80, 70, 50]
Breadth-First (Level-Order) : [50, 30, 70, 20, 40, 60, 80]
Delete 50 (root with 2 children) -> Inorder: [20, 30, 40, 60, 70, 80]
```

## Important Edge Cases Handled
- Traversing, searching, or deleting from an empty tree.
- Duplicate insertions in BST are ignored cleanly without corrupting tree order.
- Deleting a root node, leaf node, node with 1 child, node with 2 children, and non-existent node.
- Invalid tree paths (characters other than `L`/`R` or missing intermediate nodes) in general Binary Tree insertion.
- Negative integers, zero, large numbers, and invalid non-integer inputs.
