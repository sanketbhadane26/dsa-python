arr=[2,7,11,15]
num=6
n=len(arr)


for x in range(n):
    for y in range(x+1,n):
        if(arr[x]+arr[y]==num):
            print(f"two sum = {x,y}")
            found=True
            break
    if(found):
        break
if not found:
    print("No combination found")
            
    


