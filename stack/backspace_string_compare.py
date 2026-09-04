s = "a#c"
t = "b"
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        if value=='#':
            self.pop()
        else:
            self.stack.append(value)
    def pop(self):
            if self.stack:
                self.stack.pop()
stk1=Stack()
for i in s:
    stk1.push(i)
stk2=Stack()
for i in t:
    stk2.push(i)
if stk1.stack==stk2.stack:
    print("True")
else:
    print("False")




