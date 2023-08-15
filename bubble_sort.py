# bubble sort : 
# compare neighbour elements and swap if right element is greater than left element
# largest element will be at last position after first round.
# n-1 rounds required to sort array


def bubble_sort(arr):
    l = len(arr)
    for i in range(1,l):
        for j in range(l-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubble_sort([2,5,1,3,10]))


# Good approach is to find second largest element of unsorted array, perform 2 rounds


# optimization : if no swap found then break


def bubble_sort_op(arr):
    l = len(arr)
    is_swap = False
    
    for i in range(1,l):
        is_swap = False
        for j in range(l-i):
            if arr[j]>arr[j+1]:
                is_swap = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        
        if not is_swap:
            break
    return arr
        
print(bubble_sort([1,2,3,4,5,6,7,9,8]))         