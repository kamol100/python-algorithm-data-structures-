def query_fixed_length(arr, queries):

    #print(arr[:3])
    result = []
    for qu in queries:
        maxnum = max(arr[:qu])
        minnum= maxnum
        for i in range(qu, len(arr)):
            if arr[i-qu] == maxnum:
                maxnum = max(arr[i-qu+1:i+1])
            elif arr[i] > maxnum:
                maxnum = arr[i]
            if maxnum < minnum:
                minnum = maxnum
        result.append(minnum)
    return result



arr = [2,3,4,5,6]
queries = [2,3]
print(query_fixed_length(arr,queries))