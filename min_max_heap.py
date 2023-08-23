import heapq

def maxMin(operations, x):
    result = []
    max_heap = []
    min_heap = []
    
    for i in range(len(operations)):
        if operations[i] == "push":
            heapq.heappush(max_heap, -x[i])
            heapq.heappush(min_heap, x[i])
        elif operations[i] == "pop":
            max_heap.remove(-x[i])
            min_heap.remove(x[i])
            heapq.heapify(max_heap)
            heapq.heapify(min_heap)
        
        if len(max_heap) >= 1 and len(min_heap) >= 1:
            product = -max_heap[0] * min_heap[0]
            result.append(product)
        else:
            result.append(0)
    
    return result


print(maxMin(["push", "push" , "push" , "push"],[328330709,570933073,578466200,589317647]))