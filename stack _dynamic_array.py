#Static array
class StaticArray:
    def __init__(self,n):
        self.a=[None]*n; self.size=0

    def insert(self,x):
        self.a[self.size]=x; self.size+=1

arr=StaticArray(5)
arr.insert(10); arr.insert(20)
print(arr.a[:arr.size])

#dynamic array

class DynArray:
    def __init__(self): self.a=[]

    def append(self,x): self.a.append(x)

d=DynArray()
d.append(10); d.append(20)
print(d.a)