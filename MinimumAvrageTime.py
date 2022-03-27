from heapq import heappop,heappush

def minimumAverageTime(customers):
    number_of_customer = len(customers)
    total_time = waiting_time = 0
    customers.sort(reverse=True)
    queue = []
    while customers or queue:
        while customers and customers[-1][0] < total_time:
            heappush(queue, customers.pop()[::-1])
        if queue:
            task = heappop(queue)
            total_time += task[0]
            waiting_time += total_time - task[1]
        else:
            heappush(queue, customers.pop()[::-1])
            total_time = queue[0][1]
    return waiting_time // number_of_customer





customers = [[0,3],[1,9],[2,6]]
print(minimumAverageTime(customers))