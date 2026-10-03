class Queue:
    def __init__(self):
        self.queue=[]
        self.window_size=0
    def window(self,value):
        self.window_size=value
    def moving_average(self,value):
        if len(self.queue)>=self.window_size:
            self.queue.pop(0)
        self.queue.append(value)
        self.sum=0
        self.count=0
        for i in self.queue:
            self.sum=self.sum+i
            self.count=self.count+1
        print(self.sum/self.count)
        
que=Queue()
que.window(3)
que.moving_average(2)
que.moving_average(3)
que.moving_average(4)
que.moving_average(5)
que.moving_average(2)