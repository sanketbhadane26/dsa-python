arr1=[1,2,3,4]
seen={}
count=True
for i in range(len(arr1)):
    if (arr1[i] in seen):
        print("Array contains duplicate")
        count=False
        break
    seen[arr1[i]] = i
if(count):
    print("array dosent contains duplicates")


