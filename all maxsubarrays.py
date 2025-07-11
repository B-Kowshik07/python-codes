def sub_arrays(arr):
    N=len(arr)
    print([])

    for i in range(N):
        for j in range(i,N):
            subarrays=arr[i:j+1]
            print(subarrays)
arr=list(map(int,input().split()))
sub_arrays(arr)