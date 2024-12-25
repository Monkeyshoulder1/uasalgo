def floyd_cycle_detection(arr):
    """
    Detect cycle in an array using Floyd's algorithm
    
    Args:
        arr (List[int]): Input array
    
    Returns:
        int or None: Cycle start element, or None if no cycle
    """
    # Find the intersection point of the two pointers
    tortoise = arr[0]
    hare = arr[0]

    while True:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
        
        if tortoise == hare:
            break

    # Find the entrance to the cycle
    tortoise = arr[0]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]

    return tortoise

# Example usage
test_array_with_cycle = [1, 3, 4, 2, 2]  # Cycle starts at 2
print("Cycle Start Element:", floyd_cycle_detection(test_array_with_cycle))