#Queue

class Queue:
    def __init__(self): self.q=[]
    def enqueue(self,x): self.q.append(x)
    def dequeue(self): return self.q.pop(0)

q=Queue()
q.enqueue(10); q.enqueue(20)
print(q.dequeue())

#circular queue

class CQ:
    def __init__(self,n):
        self.q=[None]*n
        self.f=self.r=-1; self.n=n

    def enqueue(self,x):
        if (self.r+1)%self.n==self.f: return
        if self.f==-1: self.f=0
        self.r=(self.r+1)%self.n
        self.q[self.r]=x

    def dequeue(self):
        if self.f==-1: return
        val=self.q[self.f]
        if self.f==self.r: self.f=self.r=-1
        else: self.f=(self.f+1)%self.n
        return val

c=CQ(3)
c.enqueue(10); c.enqueue(20)
print(c.dequeue())
