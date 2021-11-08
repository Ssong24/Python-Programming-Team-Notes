import heapq

def heapsort(iterable):
    h = []
    result =[]

    # Insert all elements in heap
    for value in iterable:
        heapq.heappush(h,value)

    # Pop all elements in order and save in list
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
