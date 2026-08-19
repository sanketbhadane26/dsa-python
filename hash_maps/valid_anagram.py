s = "cats"
t = "cats"
seen1={}
seen2={}
if(len(s)!=len(t)):
    print("Strings are not valid anagrams")
    exit()
else:
    for i in range(len(s)):
        if(s[i] in seen1):
            seen1[s[i]]=seen1[s[i]]+1
        else:
            seen1[s[i]]=1
    for i in range(len(t)):
        if(t[i] in seen2):
            seen2[t[i]]=seen2[t[i]]+1
        else:
            seen2[t[i]]=1
    if(seen1==seen2):
        print("Strings are valid anagrams")
    else:
        print("Strings are not valid anagrams")




