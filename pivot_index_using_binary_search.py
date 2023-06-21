def find_pivot_index(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2
        if arr[mid - 1] > arr[mid] < arr[mid + 1]:
            return mid
        elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return -1


print(find_pivot_index([7, 9, 10, 0, 1, 2]))
