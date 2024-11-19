def quick_sort(arr):
    if len(arr) <= 1:  # Base case: Arrays of length 0 or 1 are already sorted.
        return arr
    pivot = arr[len(arr) // 2]  # Choose the pivot element (middle element of the array).
    left = [x for x in arr if x < pivot]  # All elements less than the pivot.
    middle = [x for x in arr if x == pivot]  # All elements equal to the pivot.
    right = [x for x in arr if x > pivot]  # All elements greater than the pivot.
    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort left and right, then combine.


numbers = [3, 6, 8, 10, 1, 2, 1]
sorted_numbers = quick_sort(numbers)
print("Sorted array:", sorted_numbers)
# Output: Sorted array: [1, 1, 2, 3, 6, 8, 10]
