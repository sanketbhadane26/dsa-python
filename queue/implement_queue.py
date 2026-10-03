class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if not self.queue:
            print("Queue underflow")
        else:
            return self.queue.pop(0)
    def display(self):
        if not self.queue:
            print("Queue underflow")
        else:
            print(self.queue)
    def front(self):
        if not self.queue:
            print("Queue underflow ")
        else:
            print(f"first elemet is : {self.queue[0]}")
que=Queue()
while(True):
    print("Menu ")
    print("1 Add emelent Enqueue ")
    print("2 remove element Dequeue ")
    print("3 display queue ")
    print("4 display front elemet ")
    print("5 Exit ")
    choice=int(input("Enter your choice : "))
    match(choice):
        case 1:
            value=int(input("Enter element to insert : "))
            que.enqueue(value)
        case 2:
            print(que.dequeue())
        case 3:
            que.display()
        case 4:
            que.front()
        case 5:
            break

