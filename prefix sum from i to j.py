def prefix_sum(arr):
    n=len(arr)
    result=[0]*n
    result[0]=arr[0]

    for i in range(1,n):
        result[i]=result[i-1]+arr[i]
    return result

def range_sum(result,i,j):
    if i==0:
        return result[j]
    return result[j]-result[i-1]

arr=eval(input())
i,j=map(int,input().split())
result=prefix_sum(arr)
print(range_sum(result,i,j))