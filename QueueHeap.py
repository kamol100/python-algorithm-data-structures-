from heapq import heappush, heappop

def queueHeap(operations):
    heap = []
    lookup = set()
    for query in operations:
        item  = query.split()
        if item[0] == '1':
            heappush(heap, item[1])
            lookup.add(item[1])
        if item[0] == '2':
            lookup.discard(item[1])
        if item[0] == '3':
            while heap[0] not in lookup:
                heappop(heap)
            print(heap[0])    




operations = ['1 4','1 9', '3','2 4', '3']
queueHeap(operations)