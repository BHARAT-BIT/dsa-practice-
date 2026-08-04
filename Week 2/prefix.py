def range_sum_queries(arr, queries):
    prefix = [0] * (len(arr)+1)
    prefix[0] = 0 

    for i in range(len(arr)):
        prefix[i+1] = prefix[i] + arr[i]

    result = []

    for l, r in queries:
       
            result.append(prefix[r+1] - prefix[l])

    return result

