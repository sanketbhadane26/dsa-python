nums=[1,2,3,4]
n=len(nums)
duplicate=False
for i in range(n):
    for j in range(i+1,n):
        if(nums[i]==nums[j]):
            duplicate=True
            break
if(duplicate):
    print("the array contains duplicates")
else:
    print("the array does not contains duplicates")