s = "leetcode"
seen={}
for i in range(len(s)):
    if s[i] in seen:
        seen[s[i]]=seen[s[i]]+1
    else:
        seen[s[i]]=1
for i in seen:
    if seen[i]==1:
        print(i)
        break
