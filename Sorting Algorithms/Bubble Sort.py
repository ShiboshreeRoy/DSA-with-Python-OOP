def bubble_sort(arr):
    n = len(arr)  # Get the number of elements in the array.
    for i in range(n):  # Outer loop for each pass through the array.
        for j in range(0, n - i - 1):  # Inner loop for comparing adjacent elements.
            if arr[j] > arr[j + 1]:  # If the current element is greater than the next element:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap them.


numbers = [64, 34, 25, 12, 22, 11, 90]
print(numbers)
bubble_sort(numbers)
print("Sorted array:", numbers)  # Output: Sorted array: [11, 12, 22, 25, 34, 64, 90]
