def kadane_algorithm(arr):
    """
    Find maximum subarray sum using Kadane's algorithm
    
    Args:
        arr (List[int]): Input array
    
    Returns:
        int: Maximum subarray sum
    """
    max_so_far = float('-inf')
    max_ending_here = 0

    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Example usage
test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum:", kadane_algorithm(test_array))