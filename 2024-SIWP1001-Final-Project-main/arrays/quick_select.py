def quick_select(arr, k):
    """
    Find kth smallest element using Quick Select algorithm
    
    Args:
        arr (List[int]): Input array
        k (int): Position of the element to find
    
    Returns:
        int: kth smallest element
    """
    def partition(arr, left, right):
        pivot = arr[right]
        i = left - 1

        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1

    def quick_select_helper(arr, left, right, k):
        if left == right:
            return arr[left]

        pivot_index = partition(arr, left, right)

        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quick_select_helper(arr, left, pivot_index - 1, k)
        else:
            return quick_select_helper(arr, pivot_index + 1, right, k)

    return quick_select_helper(arr, 0, len(arr) - 1, k - 1)

# Example usage
test_array = [10, 4, 5, 8, 6, 11, 26]
k = 3  # Find 3rd smallest element
print(f"{k}rd smallest element:", quick_select(test_array, k))