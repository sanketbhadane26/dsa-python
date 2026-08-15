arr = [3,1,2,10,1]
n=len(arr)
for x in range(n-1):
    running_sum=arr[x]+arr[x+1]
    arr[x+1]=running_sum
print(arr)
    