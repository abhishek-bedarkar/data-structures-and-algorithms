# 1, 2, 3, 6, 3, 2
# O(logn)
def peak_element(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2

        if arr[mid] > arr[mid + 1]:
            end = mid
        elif arr[mid] < arr[mid + 1]:
            start = mid + 1
    return end


# print(peak_element([1, 2, 3, 6, 3, 2]))

print(peak_element([18, 29, 38, 59, 98, 100, 99]))
