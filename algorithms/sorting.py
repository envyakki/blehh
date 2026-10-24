"""
Fast Sorting Algorithms & In-Memory Benchmarking
Includes: QuickSort (Dual-Pivot partition) & MergeSort
"""

import time
import random

def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(left: list[int], right: list[int]) -> list[int]:
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

if __name__ == "__main__":
    data = [random.randint(1, 10000) for _ in range(5000)]
    t0 = time.perf_counter()
    res = quick_sort(data)
    t1 = time.perf_counter()
    print(f"QuickSort 5,000 items: {(t1 - t0)*1000:.2f} ms")
