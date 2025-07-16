def rotate_array(arr,K):
    N=len(arr)
    K%=N

    return arr[K:]+arr[:K]
arr=list(map(int,input().split(',')))
K=int(input())
print(rotate_array(arr,K))