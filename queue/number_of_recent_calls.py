class Queue:
    def __init__(self):
        self.queue=[]
        self.flag=0
    def ping(self,value):
        self.queue.append(value)
        self.flag=self.flag+1
        range=value-3000
        while(self.queue and self.queue[0]<range):
                    self.queue.pop(0)
                    self.flag=self.flag-1
        return self.flag
            
que=Queue()
print(que.ping(5))
print(que.ping(1000))
print(que.ping(2500))
print(que.ping(4000))
print(que.ping(7001))

