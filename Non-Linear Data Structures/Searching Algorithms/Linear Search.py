def linear_search(arr, target):
    for i in range(len(arr)):  # Iterate through each index of the array.
        if arr[i] == target:  # Check if the current element matches the target.
            return i  # Return the index if the target is found.
    return -1  # If the loop completes and the target is not found, return -1.

numbers = [4, 2, 7, 1, 9, 3]
result = linear_search(numbers, 7)  # Searching for 7
print("Index of target:", result)  # Output: Index of target: 2

result = linear_search(numbers, 10)  # Searching for 10
print("Index of target:", result)  # Output: Index of target: -1
