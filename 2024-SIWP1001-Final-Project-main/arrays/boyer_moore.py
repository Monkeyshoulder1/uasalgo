def boyer_moore_majority(arr):
    """
    Find majority element using Boyer-Moore Voting Algorithm
    
    Args:
        arr (List[int]): Input array
    
    Returns:
        int or None: Majority element, or None if no majority
    """
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Verify candidate
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None

# Example usage
test_array1 = [2, 2, 1, 1, 1, 2, 2]  # Majority element: 2
test_array2 = [3, 3, 4, 2, 4, 4, 2, 4, 4]  # No majority element
print("Majority Element (Test Array 1):", boyer_moore_majority(test_array1))
print("Majority Element (Test Array 2):", boyer_moore_majority(test_array2))