# Given an sorted rotated array find element using binary search
# O(logn)

# 3, 5, 9, 1, 2
def find_element(arr, find):
    start = 0
    end = len(arr) - 1

    mid = start + (end - start) // 2

    while start < end:

        if arr[mid] > arr[0]:
            start = mid + 1
        else:
            end = mid
        mid = start + (end - start) // 2
    pivot_index = start

    if find >= arr[0]:
        return find_using_binary_search(arr[:pivot_index], find)
    else:
        return pivot_index + find_using_binary_search(arr[pivot_index:], find)


def find_using_binary_search(arr, find):
    start = 0
    end = len(arr)
    mid = start + (end - start) // 2

    while start < end:
        if arr[mid] == find:
            return mid
        if arr[mid] > find:
            end = mid
        else:
            start = mid + 1
        mid = start + (end - start) // 2
    return -1


print(find_element([3, 5, 6, 1, 2], 5))
print(find_element([3, 5, 6, 1, 2], 6))
