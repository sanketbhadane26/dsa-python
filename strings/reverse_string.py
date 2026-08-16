s = ["h","e","l","l","o"]
n=len(s)
j=n-1
x=0
print(s[x])
for i in s:
    temp=i
    s[x]=s[j]
    s[j]=temp
    j=j-1
    x=x+1
    if(x==n//2):
        break
print(s)
