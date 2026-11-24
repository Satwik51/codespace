# Practical 09: Heap and Priority Queue

## Practical Number
Practical 09

## Practical Title
Heap and Priority Queue

## Problem Statement
Implement a Binary Min-Heap using an array representation. Perform insertion, deletion/extract-min, and heapify operations. Extend the heap implementation to realize a Priority Queue and demonstrate the relationship between min-heaps and max-heaps.

## Concepts Used
- Complete Binary Tree represented as a 0-indexed array (`parent=(i-1)//2`, `left=2i+1`, `right=2i+2`)
- Sift-up (`heapify_up`) and Sift-down (`heapify_down`)
- Bottom-up `build_heap` (`O(n)`)
- Priority Queue extending `MinHeap` with FIFO tie-breaking sequence counter
- Min-Heap vs Max-Heap duality (`MaxHeap(S)` realized via `MinHeap(-S)`)

## Operations Implemented
- **MinHeap**: `insert`, `extract_min`, `get_min`, `delete_value`, `heapify_up`, `heapify_down`, `build_heap`, `display`
- **PriorityQueue**: `enqueue(item, priority)`, `dequeue()`, `peek()`, `display_queue()` (supports both `min` and `max` priority modes)
- `demonstrate_min_max_relationship(values)` — Demonstrates building and extracting from Min-Heap and negated-key Max-Heap.

## How to Execute
```bash
cd "/home/satwik-rai/DS USING PYTHON LAB PRACTICALS/Lab_Practicals/Practical_09"
python3 main.py
```

## Sample Input and Output
```text
Choice: 3 (Demonstrate Min-Heap vs Max-Heap)
Input: 15 3 27 8 12 1
Repeated Extract-Min      : [1, 3, 8, 12, 15, 27]
Repeated Extract-Max (-x) : [27, 15, 12, 8, 3, 1]
```

## Important Edge Cases Handled
- Underflow on `extract_min`, `get_min`, `dequeue`, or `peek` on an empty heap/queue.
- Deleting an arbitrary internal node that needs either `heapify_up` or `heapify_down`.
- Duplicate values and duplicate priorities (handled cleanly via FIFO sequence counter without type errors).
- Empty list passed to `build_heap` or Min/Max demonstration.
- Negative priorities, zero, and invalid non-integer inputs.
