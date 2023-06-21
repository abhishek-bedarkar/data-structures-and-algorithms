# O(logn)
def find_pivot_index(arr):
    start = 0
    end = len(arr) - 1
    mid = start + (end - start) // 2
    while start < end:

        if arr[mid] >= arr[0]:
            start = mid + 1
        else:
            end = mid
        mid = start + (end - start) // 2
    return start


print(find_pivot_index([7, 9, 10, 0, 1, 2]))
print(find_pivot_index([3, 8, 10, 17, 1]))
