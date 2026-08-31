nums = [0,1,0,3,12]
n=len(nums)
for i in range(n):
    for j in range(i + 1, n):        
        if nums[i]==0:
            if nums[j]!=0:
                temp=nums[j]
                nums[j]=nums[i]
                nums[i]=temp
                break
print(nums)
