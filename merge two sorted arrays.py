def merge_arrays(arr1,arr2):
    result=[]
    for num in arr1:
        result.append(num)
    for num in arr2:
        result.append(num)

    result.sort()
    return result

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
result=(merge_arrays(arr1,arr2))
print(result)
