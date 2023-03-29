# main.py

import random
from sort_algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort, heap_sort, shell_sort

if __name__ == '__main__':
    # Generate a random list of 100 numbers
    arr = [random.randint(1, 1000) for _ in range(100)]
    print(f"Original list: {arr}")

    # Sort the list using each of the sorting algorithms
    bubble_sorted = bubble_sort(arr.copy())
    print(f"Bubble sort: {bubble_sorted}")

    insertion_sorted = insertion_sort(arr.copy())
    print(f"Insertion sort: {insertion_sorted}")

    selection_sorted = selection_sort(arr.copy())
    print(f"Selection sort: {selection_sorted}")

    merge_sorted = merge_sort(arr.copy())
    print(f"Merge sort: {merge_sorted}")

    quick_sorted = quick_sort(arr.copy())
    print(f"Quick sort: {quick_sorted}")

    heap_sorted = heap_sort(arr.copy())
    print(f"Heap sort: {heap_sorted}")

    shell_sorted = shell_sort(arr.copy())
    print(f"Shell sort: {shell_sorted}")
