# Practical 01: Array ADT and Searching

## Practical Number
Practical 01

## Practical Title
Array ADT and Searching

## Problem Statement
Implement an Array ADT using a fixed-capacity Python list as the underlying storage. Perform traversal, insertion, deletion, updating, and searching operations. Implement Linear Search and Binary Search on an ordered array without using Python built-in methods that directly perform the required operations.

## Concepts Used
- Fixed-capacity Python list (`[None] * capacity`)
- Manual element shifting for insertion and deletion
- Linear Search (`O(n)`) and Binary Search (`O(log n)`) on an ordered array

## Operations Implemented
- `traverse()` — Returns active elements in order.
- `insert(index, value)` — Inserts value at `index` by shifting right.
- `delete(index)` — Removes and returns element at `index` by shifting left.
- `update(index, value)` — Updates element at `index`.
- `linear_search(target)` — Sequential search returning index or `-1`.
- `binary_search(target)` — Binary search on an ordered array returning index or `-1`.

## How to Execute
```bash
cd "/home/satwik-rai/DS USING PYTHON LAB PRACTICALS/Lab_Practicals/Practical_01"
python3 main.py
```

## Sample Input and Output
```text
After insertions : [10, 20, 30, 40]
After update     : [10, 25, 30, 40]
Deleted index 0  : 10
After deletion   : [25, 30, 40]
Linear Search 30 : 1
Binary Search 40 : 2
Binary Search 99 : -1
```

## Important Edge Cases Handled
- Non-positive capacity (`<= 0`).
- Array Overflow on full insertion and Underflow on empty deletion/update.
- Out-of-range index checks.
- Binary Search on empty array (`-1`) or unsorted array (`ValueError`).
