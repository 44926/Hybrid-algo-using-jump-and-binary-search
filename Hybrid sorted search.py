import math

def hybrid_search(arr, target):
    """
    Hybrid Search Algorithm combining Jump Search and Binary Search.
    :param arr: Sorted list of elements to search in.
    :param target: The element to search for.
    :return: Index of the target element if found, else -1.
    """
    n = len(arr)
    
    # Step 1: Jump Search Phase
    jump = int(math.sqrt(n))  # Determine the optimal jump size (sqrt of array length)
    prev = 0  # Starting index of the current block
    
    # Perform jumps to find the block where the target may be present
    while prev < n and arr[min(jump, n) - 1] < target:
        prev = jump
        jump += int(math.sqrt(n))
        if prev >= n:
            return -1  # Target not found, we are past the array bounds

    # Step 2: Binary Search Phase within the identified block
    left = prev
    right = min(jump, n) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found

# Example Array to Test the Hybrid Search Algorithm
test_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91, 105, 150, 190, 250]

# Testing the Hybrid Search with different targets
targets = [23, 72, 105, 190, 300]  # The last target (300) is not in the array
print("test array: ", test_array)

for target in targets:
    result = hybrid_search(test_array, target)
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the array.")
