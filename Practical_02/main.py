"""
Practical 02: Sorting and Binary Search
---------------------------------------
Implements Bubble Sort and Selection Sort without using Python built-in
sorting functions, implements Recursive Binary Search, and compares the
number of comparisons/operations across different input sizes.
"""

import random


def manual_copy(arr):
    """Create a shallow copy of a list manually without .copy() or slicing."""
    n = 0
    for _ in arr:
        n += 1
    copied = [None] * n
    i = 0
    while i < n:
        copied[i] = arr[i]
        i += 1
    return copied, n


def bubble_sort(arr):
    """
    Sort a list in ascending order using Bubble Sort.
    Returns (sorted_list, comparisons, swaps).
    """
    data, n = manual_copy(arr)
    comparisons = 0
    swaps = 0

    if n <= 1:
        return data, comparisons, swaps

    i = 0
    while i < n - 1:
        swapped = False
        j = 0
        while j < n - 1 - i:
            comparisons += 1
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
                swaps += 1
                swapped = True
            j += 1
        if not swapped:
            break
        i += 1

    return data, comparisons, swaps


def selection_sort(arr):
    """
    Sort a list in ascending order using Selection Sort.
    Returns (sorted_list, comparisons, swaps).
    """
    data, n = manual_copy(arr)
    comparisons = 0
    swaps = 0

    if n <= 1:
        return data, comparisons, swaps

    i = 0
    while i < n - 1:
        min_idx = i
        j = i + 1
        while j < n:
            comparisons += 1
            if data[j] < data[min_idx]:
                min_idx = j
            j += 1
        if min_idx != i:
            temp = data[i]
            data[i] = data[min_idx]
            data[min_idx] = temp
            swaps += 1
        i += 1

    return data, comparisons, swaps


def is_sorted_ascending(arr):
    """Manually check whether arr is sorted in ascending order."""
    n = len(arr)
    i = 0
    while i < n - 1:
        if arr[i] > arr[i + 1]:
            return False
        i += 1
    return True


def recursive_binary_search(arr, target, low, high, comparisons=0):
    """
    Perform Binary Search recursively on a sorted ascending list.
    Returns (index, comparisons). Returns (-1, comparisons) if not found.
    """
    if low > high:
        return -1, comparisons

    mid = low + (high - low) // 2
    comparisons += 1
    if arr[mid] == target:
        return mid, comparisons

    comparisons += 1
    if target < arr[mid]:
        return recursive_binary_search(arr, target, low, mid - 1, comparisons)
    return recursive_binary_search(arr, target, mid + 1, high, comparisons)


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


def read_int_list(prompt):
    """Read a space-separated list of integers safely (allows empty list)."""
    while True:
        raw = input(prompt).strip()
        if raw == "":
            return []
        parts = raw.split()
        result = []
        valid = True
        for token in parts:
            try:
                result.append(int(token))
            except ValueError:
                print(f"Invalid integer token: '{token}'. Please re-enter.")
                valid = False
                break
        if valid:
            return result


def compare_for_sizes(sizes, case_type):
    """
    Compare Bubble Sort, Selection Sort, and Recursive Binary Search
    for a given list of input sizes and case type ('sorted', 'reverse', 'random').
    """
    print(f"\n--- Comparison Report ({case_type.upper()} INPUT) ---")
    header = (
        f"{'Size':>6} | {'Bubble Cmp':>11} | {'Bubble Swp':>10} | "
        f"{'Select Cmp':>11} | {'Select Swp':>10} | {'BinSrch (Worst)':>15}"
    )
    print(header)
    print("-" * len(header))

    rng = random.Random(42)  # Deterministic seed for reproducible results

    for n in sizes:
        if case_type == "sorted":
            arr = [i for i in range(n)]
        elif case_type == "reverse":
            arr = [n - i for i in range(n)]
        else:
            arr = [rng.randint(-1000, 1000) for _ in range(n)]

        sorted_arr, b_cmp, b_swp = bubble_sort(arr)
        _, s_cmp, s_swp = selection_sort(arr)

        # Search for a guaranteed absent value to measure worst-case comparisons
        if n == 0:
            bs_cmp = 0
        else:
            absent_target = sorted_arr[n - 1] + 1
            _, bs_cmp = recursive_binary_search(sorted_arr, absent_target, 0, n - 1)

        print(
            f"{n:>6} | {b_cmp:>11} | {b_swp:>10} | "
            f"{s_cmp:>11} | {s_swp:>10} | {bs_cmp:>15}"
        )


def main():
    print("=== Practical 02: Sorting and Recursive Binary Search ===")
    current_array = []

    try:
        while True:
            print("\n--- Menu ---")
            print(f"Current Array: {current_array}")
            print("1. Enter / Replace Array Elements")
            print("2. Sort using Bubble Sort & Selection Sort (Compare Operations)")
            print("3. Recursive Binary Search on Current Array")
            print("4. Compare Operations Across Standard Input Sizes (0, 1, 5, 10, 50, 100, 250)")
            print("5. Compare Operations Across Custom Input Sizes")
            print("6. Exit")

            choice = read_int("Enter your choice (1-6): ")

            if choice == 1:
                current_array = read_int_list(
                    "Enter integers separated by spaces (or press Enter for empty): "
                )
                print(f"Array updated ({len(current_array)} element(s)).")

            elif choice == 2:
                b_sorted, b_cmp, b_swp = bubble_sort(current_array)
                s_sorted, s_cmp, s_swp = selection_sort(current_array)
                print("\nOriginal Array :", current_array)
                print(
                    f"Bubble Sort    : {b_sorted} | "
                    f"Comparisons = {b_cmp}, Swaps = {b_swp}"
                )
                print(
                    f"Selection Sort : {s_sorted} | "
                    f"Comparisons = {s_cmp}, Swaps = {s_swp}"
                )

                if current_array != b_sorted:
                    save = input(
                        "Update current array with sorted result? (y/n): "
                    ).strip().lower()
                    if save == "y":
                        current_array = b_sorted
                        print("Current array updated to sorted array.")

            elif choice == 3:
                if len(current_array) == 0:
                    print("Array is empty. Binary search returns -1 (0 comparisons).")
                    continue
                if not is_sorted_ascending(current_array):
                    print("Array is not sorted. Sorting first using Selection Sort...")
                    current_array, _, _ = selection_sort(current_array)
                    print("Sorted Array:", current_array)

                target = read_int("Enter target integer to search: ")
                idx, comps = recursive_binary_search(
                    current_array, target, 0, len(current_array) - 1
                )
                if idx != -1:
                    print(
                        f"Found {target} at index {idx} in {comps} comparison(s)."
                    )
                else:
                    print(
                        f"{target} not found in array ({comps} comparison(s))."
                    )

            elif choice == 4:
                standard_sizes = [0, 1, 5, 10, 50, 100, 250]
                compare_for_sizes(standard_sizes, "sorted")
                compare_for_sizes(standard_sizes, "random")
                compare_for_sizes(standard_sizes, "reverse")

            elif choice == 5:
                raw_sizes = read_int_list(
                    "Enter non-negative input sizes separated by spaces (e.g. 5 20 50): "
                )
                if len(raw_sizes) == 0:
                    print("No sizes provided.")
                    continue
                valid_sizes = []
                invalid = False
                for sz in raw_sizes:
                    if sz < 0:
                        print(f"Invalid size {sz}: size cannot be negative.")
                        invalid = True
                        break
                    if sz > 5000:
                        print(
                            f"Size {sz} is very large for O(n^2) sorts; "
                            "please use sizes <= 5000."
                        )
                        invalid = True
                        break
                    valid_sizes.append(sz)
                if invalid:
                    continue

                print("Select input pattern:")
                print("1. Already Sorted (Best Case for Bubble Sort)")
                print("2. Random / Mixed")
                print("3. Reverse Sorted (Worst Case)")
                pat = read_int("Enter pattern choice (1-3): ")
                if pat == 1:
                    compare_for_sizes(valid_sizes, "sorted")
                elif pat == 2:
                    compare_for_sizes(valid_sizes, "random")
                elif pat == 3:
                    compare_for_sizes(valid_sizes, "reverse")
                else:
                    print("Invalid pattern choice.")

            elif choice == 6:
                print("Exiting Practical 02. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

    except (EOFError, KeyboardInterrupt):
        print("\nProgram interrupted. Exiting cleanly.")


if __name__ == "__main__":
    main()
