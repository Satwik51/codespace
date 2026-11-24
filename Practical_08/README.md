# Practical 08: Hash Table

## Practical Number
Practical 08

## Practical Title
Hash Table

## Problem Statement
Implement a fixed-size Hash Table using a suitable hash function. Perform insertion, searching, and deletion using separate chaining. Demonstrate an open-addressing collision-resolution method such as linear probing.

## Concepts Used
- Modular hash function (`key % capacity` for integers; polynomial rolling hash for strings)
- Collision resolution via Separate Chaining (user-defined `ChainNode` linked lists)
- Collision resolution via Open Addressing (Linear Probing `(hash(key) + i) % capacity`)
- Tombstone (`<DELETED>`) markers to preserve probe chains after deletion

## Operations Implemented
- **SeparateChainingHashTable**: `insert(key, value)`, `search(key)`, `delete(key)`, `display()`
- **LinearProbingHashTable**: `insert(key, value)`, `search(key)`, `delete(key)`, `display()`

## How to Execute
```bash
cd "/home/satwik-rai/DS USING PYTHON LAB PRACTICALS/Lab_Practicals/Practical_08"
python3 main.py
```

## Sample Input and Output
```text
Mode: Linear Probing, Capacity: 5
Insert (10, 'A') -> Inserted key '10' at slot 0 (probes: [0]).
Insert (15, 'B') -> Inserted key '15' at slot 1 (probes: [0, 1]).
Delete (10)      -> Deleted (10: 'A') from slot 0 (marked <DELETED>).
Search (15)      -> Found at slot 1: 15 -> 'B' (probes: [0, 1])
```

## Important Edge Cases Handled
- Hash table capacity `<= 0` rejected.
- Table Overflow in Linear Probing when all slots are occupied.
- Updating existing keys instead of creating duplicate entries (even across `<DELETED>` slots).
- Reusing `<DELETED>` slots safely during insertion and continuing past `<DELETED>` during search.
- Negative integer keys, zero, very large keys, and string/special-character keys.
- Empty keys/values and invalid menu selections.
