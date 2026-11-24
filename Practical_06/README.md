# Practical 06: Doubly and Circularly Linked Lists

## Practical Number
Practical 06

## Practical Title
Doubly and Circularly Linked Lists

## Problem Statement
Implement Doubly Linked List and Circularly Linked List using node objects and references. Perform insertion and deletion operations and appropriate traversals, including forward and backward traversal of a Doubly Linked List.

## Concepts Used
- Doubly Linked List (`prev`, `data`, `next`) with `head` and `tail` references
- Forward (`head -> tail`) and Backward (`tail -> head`) traversal
- Singly Circularly Linked List (`tail.next = head`)
- Safe circular traversal termination without infinite loops

## Operations Implemented
- **DoublyLinkedList**: `insert_at_beginning`, `insert_at_end`, `insert_at_position`, `delete_from_beginning`, `delete_from_end`, `delete_at_position`, `delete_by_value`, `search`, `traverse_forward`, `traverse_backward`
- **CircularLinkedList**: `insert_at_beginning`, `insert_at_end`, `insert_at_position`, `delete_from_beginning`, `delete_from_end`, `delete_at_position`, `delete_by_value`, `search`, `traverse`

## How to Execute
```bash
cd "/home/satwik-rai/DS USING PYTHON LAB PRACTICALS/Lab_Practicals/Practical_06"
python3 main.py
```

## Sample Input and Output
```text
Doubly Linked List: Insert at End 10, 20, 30
Forward : None <- 10 <-> 20 <-> 30 -> None
Backward: None <- 30 <-> 20 <-> 10 -> None

Circularly Linked List: Insert at End 1, 2, 3
Traverse: HEAD -> 1 -> 2 -> 3 -> (back to HEAD: 1)
```

## Important Edge Cases Handled
- Empty list deletion, search, and traversal.
- Single-node list deletion (correctly resets `head` and `tail` to `None`, avoiding self-loop dangling nodes).
- Out-of-range 1-based positions.
- Value not found during `delete_by_value` and `search`.
- Invalid non-integer input and menu choices.
