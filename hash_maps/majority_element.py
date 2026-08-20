nums = [2,2,1,1,1,2,2]
n=len(nums)
seen={}
for i in range(n):
    if(nums[i] in seen):
        seen[nums[i]]=seen[nums[i]]+1
    else:
        seen[nums[i]]=1
for i in seen:
    if(seen[i]>n//2):
        print(f"{i} is the majority element of the array")
