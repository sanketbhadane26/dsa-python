s = "A man, a plan, a canal: Panama"
cleaned=""
for i in s:
    if(i.isalnum()):
        cleaned=cleaned+i
cleaned=cleaned.lower()
n=len(cleaned)
y=n-1
reversed_str=""
for i in range(n):
    reversed_str=reversed_str+cleaned[y]
    y=y-1
if(reversed_str==cleaned):
    print("String is palindrome")
else:
    print("String iis not a Palindrome")
