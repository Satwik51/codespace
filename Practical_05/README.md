# Practical 05: Singly Linked List

## Practical Number
Practical 05

## Practical Title
Singly Linked List

## Problem Statement
Implement a Singly Linked List using a user-defined `Node` class and references. Perform insertion at the beginning, end, and specified position; deletion, searching, traversal, and reversal.

## Concepts Used
- Dynamic memory nodes (`Node(data, next)`)
- Pointer/reference manipulation (`head`)
- 1-based positional insertion and deletion
- Linear search across linked nodes
- Iterative three-pointer in-place reversal (`prev`, `curr`, `next_node`)

## Operations Implemented
- `insert_at_beginning(data)`
- `insert_at_end(data)`
- `insert_at_position(pos, data)`
- `delete_from_beginning()`
- `delete_from_end()`
- `delete_at_position(pos)`
- `delete_by_value(target)`
- `search(target)`
- `traverse()`
- `reverse()`

## How to Execute
```bash
cd "/home/satwik-rai/DS USING PYTHON LAB PRACTICALS/Lab_Practicals/Practical_05"
python3 main.py
```

## Sample Input and Output
```text
Insert at End: 10, 20, 30
Insert at Beginning: 5
Insert at Position 3: 15
Traverse -> HEAD -> 5 -> 10 -> 15 -> 20 -> 30 -> None
Search 15 -> Found 15 at 1-based position(s): [3]
Reverse -> HEAD -> 30 -> 20 -> 15 -> 10 -> 5 -> None
```

## Important Edge Cases Handled
- Deleting, searching, or reversing an empty list.
- Single-node list insertion, deletion (from beginning/end/position 1), and reversal.
- Out-of-range positions (`pos < 1` or `pos > size + 1` for insert; `pos > size` for delete).
- Duplicate values (search returns all matching 1-based positions).
- Non-integer inputs and invalid menu choices.
