s = "leetcode"
n=len(s)
index=-1
for i in range(n):
    for j in range(i+1,n):
        if s[i]==s[j]:
            break
    else:
        index=i
        break
print(index)

