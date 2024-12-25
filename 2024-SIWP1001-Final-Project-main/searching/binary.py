def binary_search(arr, target):
    """
    Perform binary search on a sorted array
    
    Args:
        arr (List[int]): Sorted input array
        target (int): Element to find
    
    Returns:
        int or None: Index of target if found, None otherwise
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target was not present in the array
    return None

# Example usage with sorted array
sorted_array = [1, 3, 4, 6, 8, 9, 11, 15]
target = 6
result = binary_search(sorted_array, target)
print(f"Target {target} found at index: {result}")

# Example with target not in array
target_not_found = 7
result_not_found = binary_search(sorted_array, target_not_found)
print(f"Target {target_not_found} found at index: {result_not_found}")