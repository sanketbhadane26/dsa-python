class Queue:
    def __init__(self):
        self.queue=[]
    def add(self,value):
        self.queue.append(value)
    def time_required(self,k):
        self.count=0
        while(1):
            self.queue[0]=self.queue[0]-1
            self.count=self.count+1
            if(self.queue[0]==0):
                if(k==0):
                    print(self.count)
                    break
                else:
                    self.queue.pop(0)
                    k=k-1
            else:
                    self.queue.append(self.queue[0])
                    self.queue.pop(0)
                    if(k==0):
                        k=len(self.queue)-1 
                    else:
                        k=k-1  
que=Queue()
que.add(5)
que.add(1) 
que.add(1)
que.add(1)
que.time_required(0 )