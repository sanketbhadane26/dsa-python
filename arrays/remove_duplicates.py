arr = [0,0,1,1,1,2,2,3,3,4]
n = len(arr)
i = 0

for j in range(1, n):
    if arr[i] != arr[j]:
        i = i + 1
        arr[i] = arr[j]

k = i + 1

print(arr)
print("Number of unique elements:", k)