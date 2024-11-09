import math
import time

# Binary Search Implementation
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Jump Search Implementation
def jump_search(arr, target):
    n = len(arr)
    jump = int(math.sqrt(n))
    prev = 0

    # Finding the block where the element may be present
    while arr[min(jump, n) - 1] < target:
        prev = jump
        jump += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search within the identified block
    for i in range(prev, min(jump, n)):
        if arr[i] == target:
            return i
    return -1

# Hybrid Search Implementation
def hybrid_search(arr, target):
    n = len(arr)
    jump = int(math.sqrt(n))
    prev = 0

    # Step 1: Jump Search Phase
    while prev < n and arr[min(jump, n) - 1] < target:
        prev = jump
        jump += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Step 2: Binary Search Phase within the identified block
    left = prev
    right = min(jump, n) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Function to measure the execution time of different search algorithms
def measure_search_time(search_func, arr, target):
    start_time = time.time()
    result = search_func(arr, target)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

# Example Array
test_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91, 105, 150, 190, 250, 300, 350, 400, 450, 500]
targets = [23, 72, 105, 190, 500, 600]  # 600 is not in the array

# Testing and Timing the Searches
for target in targets:
    print(f"\nSearching for {target}:")

    # Measure Binary Search Time
    result, time_taken = measure_search_time(binary_search, test_array, target)
    if result != -1:
        print(f"Binary Search: Found at index {result} in {time_taken:.6f} seconds")
    else:
        print(f"Binary Search: Not found in {time_taken:.6f} seconds")

    # Measure Jump Search Time
    result, time_taken = measure_search_time(jump_search, test_array, target)
    if result != -1:
        print(f"Jump Search: Found at index {result} in {time_taken:.6f} seconds")
    else:
        print(f"Jump Search: Not found in {time_taken:.6f} seconds")

    # Measure Hybrid Search Time
    result, time_taken = measure_search_time(hybrid_search, test_array, target)
    if result != -1:
        print(f"Hybrid Search: Found at index {result} in {time_taken:.6f} seconds")
    else:
        print(f"Hybrid Search: Not found in {time_taken:.6f} seconds")
