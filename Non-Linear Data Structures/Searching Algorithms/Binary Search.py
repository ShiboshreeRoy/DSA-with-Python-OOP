def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Define the initial search boundaries: left (start) and right (end).
    while left <= right:  # Continue searching while the range is valid.
        mid = (left + right) // 2  # Calculate the middle index of the current range.
        if arr[mid] == target:  # If the middle element is the target, return the index.
            return mid
        elif arr[mid] < target:  # If the target is greater, discard the left half.
            left = mid + 1
        else:  # If the target is smaller, discard the right half.
            right = mid - 1
    return -1  # If the target is not found, return -1.

numbers = [1, 3, 5, 7, 9, 11]
result = binary_search(numbers, 7)  # Searching for 7
print("Index of target:", result)  # Output: Index of target: 3

result = binary_search(numbers, 4)  # Searching for 4
print("Index of target:", result)  # Output: Index of target: -1
