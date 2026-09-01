class stack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if not self.stack:
            print("stack is empty")
        else:
            value = self.stack.pop()
            print(f"value deleted is {value}")
    def peek(self):
        if not self.stack:
            print("stack is empty")
        else:
            print(self.stack[-1])
    def is_empty(self):
        return len(self.stack) == 0
stk_obj=stack()
while(1):
    print("choice Menu : ")
    print("1 push ")
    print("2 pop ")
    print("3 peek ")
    print("4 is empty ")
    print("5 exit ")
    user_input=int(input("Enter a choice : "))
    match user_input:
        case 1:
            value=int(input("Enter element to insert :"))
            stk_obj.push(value)
        case 2:
            stk_obj.pop()
        case 3:
            stk_obj.peek()
        case 4:
            print(stk_obj.is_empty())
        case 5:
            break

        
