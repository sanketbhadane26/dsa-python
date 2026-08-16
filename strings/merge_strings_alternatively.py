word1 = "abcde"
word2 = "pq"
merged=""
x=0
y=0
n=len(word1)
m=len(word2)
if(m>n):
    iterate=m
else:
    iterate=n
for i in range(iterate):
    if(i<len(word1)):
        merged=merged+word1[i]
    if(y<len(word2)):
        merged=merged+word2[y]
        y=y+1
print(merged)




