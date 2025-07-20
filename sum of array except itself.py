def sum_of_numbers(arr):
    n=len(arr)
    result=[]

    total=0
    for i in range(n):
        total+=arr[i]

    for i in range(n):
        value=total-arr[i]
        result.append(value)

    return result

arr=eval(input())
print(sum_of_numbers(arr))