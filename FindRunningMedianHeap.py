
from heapq import heappush,heappop

def findMedian(a):
    min_heap = []
    max_heap = []
    result = []
    def addItem(item, min_heap, max_heap):
        if not max_heap or item < -max_heap[0]:
            heappush(max_heap, -item)
        else:
            heappush(min_heap, item)

        if len(min_heap) > len(max_heap)+1:
            heappush(max_heap, -heappop(min_heap))

        if len(max_heap) > len(min_heap)+1:
            heappush(min_heap, -heappop(max_heap))

        print('min',min_heap)
        print('max',max_heap)
        print(median(max_heap,max_heap))
        print("-------------")

    def median(min_heap, max_heap):
        if len(min_heap) == len(max_heap):
            return (min_heap[0] - max_heap[0])/2

        if len(min_heap) > len(max_heap):
            return float(min_heap[0])
        else:
            return float(-max_heap[0])

    for item in a:
        addItem(item, min_heap, max_heap)
        print(median(min_heap, max_heap))
        result.append(median(min_heap,max_heap))
    return result




a = [7,3,5,2]
print(findMedian(a))
print("=============================================")
b = [12,4,5,3,8,7]
print(findMedian(b))