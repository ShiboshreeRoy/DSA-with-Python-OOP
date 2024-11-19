def merge_sort(arr):
    if len(arr) > 1:  # Proceed only if the array has more than one element.
        mid = len(arr) // 2  # Find the middle index to divide the array.
        left = arr[:mid]  # Create the left sub-array.
        right = arr[mid:]  # Create the right sub-array.

        merge_sort(left)  # Recursively sort the left sub-array.
        merge_sort(right)  # Recursively sort the right sub-array.

        i = j = k = 0  # Initialize pointers for left, right, and merged arrays.

        # Merge the two sorted sub-arrays.
        while i < len(left) and j < len(right):
            if left[i] < right[j]:  # Compare elements from left and right.
                arr[k] = left[i]  # If left element is smaller, add it to the merged array.
                i += 1
            else:
                arr[k] = right[j]  # Otherwise, add the right element.
                j += 1
            k += 1

        # Add any remaining elements from the left sub-array.
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Add any remaining elements from the right sub-array.
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

numbers = [38, 27, 43, 3, 9, 82, 10]
merge_sort(numbers)
print("Sorted array:", numbers)
# Output: Sorted array: [3, 9, 10, 27, 38, 43, 82]
numbers = [38, 27, 43, 3, 9, 82, 10]
merge_sort(numbers)
print("Sorted array:", numbers)
# Output: Sorted array: [3, 9, 10, 27, 38, 43, 82]
