# Practical 04: Linear and Circular Queues

## Practical Number
Practical 04

## Practical Title
Linear and Circular Queues

## Problem Statement
Implement Linear Queue and Circular Queue using fixed-capacity Python lists with explicit `front` and `rear`. Implement `enqueue`, `dequeue`, and `peek` operations, including overflow and underflow conditions.

## Concepts Used
- FIFO (First-In, First-Out) Queue ADT
- Explicit `front` and `rear` index pointers on fixed-capacity arrays
- Linear Queue limitation (false overflow when `rear == capacity - 1` even if slots before `front` were freed)
- Circular Queue modulo arithmetic `(rear + 1) % capacity` and `(front + 1) % capacity`

## Operations Implemented
- `LinearQueue`: `enqueue()`, `dequeue()`, `peek()`, `is_empty()`, `is_full()`, `display()`
- `CircularQueue`: `enqueue()`, `dequeue()`, `peek()`, `is_empty()`, `is_full()`, `display()`

## How to Execute
```bash
cd "/home/satwik-rai/DS USING PYTHON LAB PRACTICALS/Lab_Practicals/Practical_04"
python3 main.py
```

## Sample Input and Output
```text
Select Queue: 2 (Circular Queue), Capacity: 3
Enqueue: A, B, C
Dequeue -> Dequeued: 'A'
Enqueue: D -> Enqueued 'D' (wraps around to index 0!)
Display -> Circular Queue (front -> rear): [B, C, D] | front = 1, rear = 0, slots = ['D', 'B', 'C']
```

## Important Edge Cases Handled
- Zero or negative capacity rejected.
- Single-element capacity (`capacity = 1`) handled accurately for both Linear and Circular Queues.
- Overflow when queue is full and Underflow on `dequeue`/`peek` when empty.
- Resetting `front = rear = -1` when the last element is dequeued.
- Empty input values and invalid menu choices.
