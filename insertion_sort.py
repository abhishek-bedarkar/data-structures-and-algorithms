# insertion sort

def insertion_sort(arr):
    l = len(arr)
    
    if l <=1:
        return arr
    for i in range(1,l):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


print(insertion_sort([10,9,8,6,3,1]))