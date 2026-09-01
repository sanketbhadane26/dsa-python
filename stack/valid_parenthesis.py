s = "([)]"
stk=[]
pairs = {
    ")": "(",
    "}": "{",
    "]": "["
}
result=True
for i in range(len(s)):
    if s[i] in "([{":
        stk.append(s[i])   
    else: 
        if not stk:
            result=False
            break
        top=stk[-1]
        if pairs[s[i]]!=top: 
            result=False
            break
        else:
            stk.pop()
            
print(result)

            

        

