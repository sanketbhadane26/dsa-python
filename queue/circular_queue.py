class MyCircularQueue:
    def __init__(self):
        self.size=5
        self.circular_queue=[None]*5
        self.front_index=-1
        self.rear_index=-1
    def enqueue(self,value):
        if((self.rear_index+1)%self.size==self.front_index):
            print("Overflow")
        elif(self.front_index==-1 and self.rear_index==-1):
            self.front_index+=1
            self.rear_index+=1
            self.circular_queue[self.rear_index]=value
            print(f' value inserted ')
        else:
            self.rear_index=(self.rear_index+1)%self.size
            self.circular_queue[self.rear_index]=value
            print(f' value inserted ')
    def dequeue(self):
        if(self.front_index==-1 and self.rear_index==-1):
            print("underflow")
        elif(self.front_index==self.rear_index):
            print(f"Element {self.circular_queue[self.front_index]} Popped")
            self.circular_queue[self.front_index]=None
            self.front_index=-1
            self.rear_index=-1
        else:
            print(f"Element {self.circular_queue[self.front_index]} Popped")
            self.circular_queue[self.front_index]=None
            self.front_index=(self.front_index+1)%self.size
    def front(self):
        if(self.front_index==-1 and self.rear_index==-1):
            print("underflow")
        else:
           print(f"front {self.circular_queue[self.front_index]} ")
    def rear(self):
        if(self.front_index==-1 and self.rear_index==-1):
            print("underflow")
        else:
            print(f"rear {self.circular_queue[self.rear_index]} ")
    def isempty(self):
        if(self.front_index==-1 and self.rear_index==-1):
            print("Queue is Empty ")
        else:
            print("Queue is Not Empty")
    def isfull(self):
        if((self.rear_index+1)%self.size==self.front_index):
            print("Queue is full ")
        else:
            print("Queue is Not full ")
que=MyCircularQueue()
while(1):
    print("Menu : ")
    print("1. Enqueue ")
    print("2. Dequeue ")
    print("3. Check Front ")
    print("4. Check Rear ")
    print("5. Check Queue is full? ")
    print("6. check queue is empty? ")
    print("7. Exit ")
    choice=int(input("Enter your choice : "))
    match choice:
        case 1:
            value=int(input("Enter a value : "))
            que.enqueue(value)
        case 2:
            que.dequeue()
        case 3:
            que.front()
        case 4:
            que.rear()
        case 5:
            que.isfull()
        case 6:
            que.isempty()
        case 7:
            print("Exiting..")
            break
        case _:
            print("Invalid choice ")
        


    


