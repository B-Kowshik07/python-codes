def find_pairs(arr,K):
    seen=set()
    pairs=[]

    for nums in arr:
         needed=K-nums
         if needed in seen:
                pairs.append(tuple(sorted([needed,nums])))
         seen.add(nums)
    return pairs

arr=list(map(int,input("Enter numbers: ").split()))
K=int(input())

pairs=(find_pairs(arr,K))
for R in pairs:
    print(R)
