
# 1. First and last position in array :
#  [0,1,6,6,6,7]
#  O(2logn)
def binary_search_first_position(arr, find):
    start = 0
    end = len(arr) - 1

    first_position = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == find:
            first_position = mid
            end = mid - 1
        elif arr[mid] > find:
            end = mid - 1
        else:
            start = mid + 1
    return first_position


print(binary_search_first_position([0, 1, 6, 6, 6, 7], 6))


def binary_search_last_position(arr, find):
    start = 0
    end = len(arr) - 1

    last_position = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == find:
            last_position = mid
            start = mid + 1
        elif arr[mid] > find:
            end = mid - 1
        else:
            start = mid + 1
    return last_position


print(binary_search_last_position([0, 1, 6, 6, 6, 7], 6))
