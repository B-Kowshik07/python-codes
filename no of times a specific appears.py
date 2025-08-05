N=int(input("Enter the size of an array :"))

array=list(map(int,input("Enters the numbers: ").split()))

target=int(input("Enter the number to search: "))

count=0

for elements in array:
    if target==elements:
        count+=1

print(count)
