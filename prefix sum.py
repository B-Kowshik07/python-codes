def prefix_sum(arr):
    n=len(arr)
    result=[0]*n
    result[0]=arr[0]

    for i in range(1,n):
        result[i]=result[i-1]+arr[i]
    return result

arr=eval(input())
print(prefix_sum(arr))
