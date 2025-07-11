def maximum_subarray(arr):
    max_sum=curr_sum=arr[0]
    start=end=temp=0

    for i in range(len(arr)):
        if arr[i]>curr_sum+arr[i]:
            curr_sum=arr[i]
            temp=i
        else:
            curr_sum+=arr[i]

    if curr_sum>max_sum:
        max_sum=curr_sum
        start=temp
        end=i

    subarray=arr[start:end+1]
    return subarray
arr=list(map(int,input().split()))
subarray=maximum_subarray(arr)
print(f"maximim sub array{subarray}")