# Practical 02: Sorting and Binary Search

## Practical Number
Practical 02

## Practical Title
Sorting and Binary Search

## Problem Statement
Implement Bubble-Sort and Selection-Sort without using built-in sorting functions. Implement Binary Search using recursion and compare the number of comparisons/operations for different input sizes.

## Concepts Used
- Bubble Sort (`O(n^2)` worst/average, `O(n)` best case with early-exit flag)
- Selection Sort (`O(n^2)` comparisons, at most `n - 1` swaps)
- Recursive Binary Search (`O(log n)`)
- Operation counting (comparisons and swaps) across varying input sizes and patterns

## Operations Implemented
- `bubble_sort(arr)` — Manual Bubble Sort returning sorted array, comparison count, and swap count.
- `selection_sort(arr)` — Manual Selection Sort returning sorted array, comparison count, and swap count.
- `recursive_binary_search(arr, target, low, high)` — Recursive Binary Search returning index and comparison count.
- `compare_for_sizes(sizes, case_type)` — Generates comparison tables across input sizes for already sorted, random, and reverse-sorted arrays.

## How to Execute
```bash
cd "/home/satwik-rai/DS USING PYTHON LAB PRACTICALS/Lab_Practicals/Practical_02"
python3 main.py
```

## Sample Input and Output
```text
Choice: 1 -> Enter integers: 64 25 12 22 11
Choice: 2 ->
Original Array : [64, 25, 12, 22, 11]
Bubble Sort    : [11, 12, 22, 25, 64] | Comparisons = 10, Swaps = 10
Selection Sort : [11, 12, 22, 25, 64] | Comparisons = 10, Swaps = 3

Choice: 3 -> Search 22:
Found 22 at index 2 in 1 comparison(s).

Choice: 4 -> Standard Input Sizes Comparison Report (0, 1, 5, 10, 50, 100, 250)
```

## Important Edge Cases Handled
- Empty array (`[]`) and single-element array (`[42]`).
- Already sorted arrays (Bubble Sort terminates in `n - 1` comparisons, `0` swaps).
- Reverse-sorted arrays (maximum swaps/comparisons).
- Duplicate values, negative integers, zero, and very large numbers.
- Target not found in Recursive Binary Search.
- Unsorted array passed to Binary Search is detected and sorted automatically before searching.
- Invalid non-integer tokens, negative sizes, and invalid menu choices.
