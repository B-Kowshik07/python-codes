def move_zeroes(arr):
    result=[num for num in arr if num !=0]
    result+=[0]*(len(arr)-len(result))
    return  result

arr=eval(input())
print(move_zeroes(arr))