s = "A man, a plan, a canal: Panama"
formatted=""
for i in s:
    if i.isalnum():
        formatted=formatted+i
formatted=formatted.lower()
n=len(formatted)
j=n-1
result=True
for i in range(n//2):
    if(formatted[i]!=formatted[j]):
        result=False
        break
    j=j-1
if(result):
    print("given string is palindrome")
else:
    print("given string is not palindrome")

