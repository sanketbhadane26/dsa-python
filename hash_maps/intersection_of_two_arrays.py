nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
nums2_set=set(nums2)
intersection=set()
for i in range(len(nums1)):
    if(nums1[i] in nums2_set):
        intersection.add(nums1[i])
print(intersection)

