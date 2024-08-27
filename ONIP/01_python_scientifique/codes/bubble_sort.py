def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


unsorted_list = [64, 34, 25, 12, 22, 11, 90]

# Expected output: [11, 12, 22, 25, 34, 64, 90]
print("Sorted list:", bubble_sort(unsorted_list))
