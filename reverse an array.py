def reverese_array(arr):
    left=0
    right=len(arr)-1

    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
arr=input().split()
arr=reverese_array(arr)
print(" ".join(arr))