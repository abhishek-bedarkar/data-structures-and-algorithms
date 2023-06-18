# Time complexity : O(logn)
# Given : Array is in sorted order
def binary_search(arr, find):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2  # optimization for max range of int variable
        if arr[mid] == find:
            return mid
        elif arr[mid] < find:
            start = mid + 1
        else:
            end = mid - 1
    return -1


# print(binary_search([1, 20, 35, 46, 54, 55], 55))
