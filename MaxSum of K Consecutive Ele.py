def sum_max(arr,k):
    n=len(arr)
    if n<k:
        return None
    window_sum=0
    for i in range(k):
        window_sum+=arr[i]

    max_sum=window_sum

    for i in range(k,n):
        window_sum+=arr[i]-arr[i-1]
        max_sum=max(max_sum,window_sum)

    return max_sum

arr=eval(input())
k=int(input())
print(sum_max(arr,k))