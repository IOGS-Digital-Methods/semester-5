def binary_search(arr, low, high, x):
    if high < low:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binary_search(arr, low, mid - 1, x)
    else:
        return binary_search(arr, mid + 1, high, x)

sorted_list = [2, 3, 4, 10, 40]
x = 10

result = binary_search(sorted_list, 0, len(sorted_list) - 1, x)
if result != -1:
    print(f"{x} is present at index {result}")
else:
    print(f"{x} is not present in list")