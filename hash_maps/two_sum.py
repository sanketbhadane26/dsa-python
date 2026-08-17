arr=[2,7,11,15]
num=9
dict={}
n=len(arr)
for i in range(n):
    differnece=num-arr[i]
    if(differnece in dict):
        print(f"two sum found at [{dict[differnece]},{i}]")
    else:
        dict[arr[i]] = i
        


