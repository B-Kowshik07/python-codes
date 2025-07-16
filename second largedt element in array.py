def second_largest(arr):
    if len(arr)<2:
        return None
    first=second=float('-inf')
    for num in arr:
        if num>first:
            second=first
            first=num
        elif first>num>second:
            second=num
    return second
arr=list(map(int,input().split()))
print(second_largest(arr))
