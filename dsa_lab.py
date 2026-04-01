def fact_rec(n):
    if n <= 1: return 1
    return n * fact_rec(n-1)

print(fact_rec(5))

def fact_iter(n):
    res = 1
    for i in range(1, n+1): res *= i
    return res

print(fact_iter(5))

def fib_rec(n):
    if n <= 1: return n
    return fib_rec(n-1) + fib_rec(n-2)

print([fib_rec(i) for i in range(6)])

def fib_iter(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=" ")
        a,b=b,a+b

fib_iter(6)

#Stack
class Stack:
    def __init__(self): self.s=[]
    def push(self,x): self.s.append(x)
    def pop(self): return self.s.pop()

st=Stack()
st.push(10); st.push(20)
print(st.pop())

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

#Singly linked list

class Node:
    def __init__(self,d):
        self.data=d; self.next=None

class LL:
    def __init__(self): self.head=None
    def insert(self,x):
        new=Node(x); new.next=self.head
        self.head=new

l=LL()
l.insert(10); l.insert(20)

t=l.head
while t: print(t.data,end=" "); t=t.next

#Doubly linked list

class Node:
    def __init__(self,d):
        self.data=d; self.prev=self.next=None

class DLL:
    def __init__(self): self.head=None
    def insert(self,x):
        new=Node(x)
        if self.head: self.head.prev=new; new.next=self.head
        self.head=new

d=DLL()
d.insert(10); d.insert(20)
print(d.head.data)

#Circular linked list

class Node:
    def __init__(self,d):
        self.data=d; self.next=None

class CLL:
    def __init__(self): self.tail=None
    def insert(self,x):
        new=Node(x)
        if not self.tail:
            self.tail=new; new.next=new
        else:
            new.next=self.tail.next
            self.tail.next=new
            self.tail=new

c=CLL()
c.insert(10); c.insert(20)
print(c.tail.next.data)

#Binary tree
class Node:
    def __init__(self, x):
        self.data = x
        self.left = self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)

# Function Call
inorder(root)

#BST insert

class Node:
    def __init__(self, x):
        self.data = x
        self.left = self.right = None

def insert(root, x):
    if not root:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)

# Function Call
inorder(root)
#BST Delete

def delete(root, x):
    if not root: return root

    if x < root.data:
        root.left = delete(root.left, x)
    elif x > root.data:
        root.right = delete(root.right, x)
    else:
        if not root.left: return root.right
        if not root.right: return root.left

        temp = root.right
        while temp.left:
            temp = temp.left
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root



root = delete(root, 50)

# After delete (50 replaced by 70 or successor)

inorder(root)
#min heap
class MinHeap:
    def __init__(self):
        self.h = []

    # INSERT
    def insert(self, x):
        self.h.append(x)
        i = len(self.h)-1
        while i>0 and self.h[(i-1)//2] > self.h[i]:
            self.h[i], self.h[(i-1)//2] = self.h[(i-1)//2], self.h[i]
            i = (i-1)//2

    # HEAPIFY (down)
    def heapify(self, i):
        smallest = i
        l = 2*i+1
        r = 2*i+2

        if l<len(self.h) and self.h[l] < self.h[smallest]:
            smallest = l
        if r<len(self.h) and self.h[r] < self.h[smallest]:
            smallest = r

        if smallest != i:
            self.h[i], self.h[smallest] = self.h[smallest], self.h[i]
            self.heapify(smallest)

    # DELETE (extract min)
    def delete(self):
        if len(self.h)==0: return None
        if len(self.h)==1: return self.h.pop()

        root = self.h[0]
        self.h[0] = self.h.pop()
        self.heapify(0)
        return root
    
h = MinHeap()

h.insert(3)
h.insert(1)
h.insert(5)

print("Heap:", h.h)
print("Delete:", h.delete())
print("After delete:", h.h)

#Tree view
import heapq

h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)
heapq.heappush(h, 5)

print(h)
#Max heap

class MaxHeap:
    def __init__(self):
        self.h = []

    def insert(self, x):
        self.h.append(x)
        i = len(self.h)-1
        while i>0 and self.h[(i-1)//2] < self.h[i]:
            self.h[i], self.h[(i-1)//2] = self.h[(i-1)//2], self.h[i]
            i = (i-1)//2

    def heapify(self, i):
        largest = i
        l = 2*i+1
        r = 2*i+2

        if l<len(self.h) and self.h[l] > self.h[largest]:
            largest = l
        if r<len(self.h) and self.h[r] > self.h[largest]:
            largest = r

        if largest != i:
            self.h[i], self.h[largest] = self.h[largest], self.h[i]
            self.heapify(largest)

    def delete(self):
        if len(self.h)==0: return None
        if len(self.h)==1: return self.h.pop()

        root = self.h[0]
        self.h[0] = self.h.pop()
        self.heapify(0)
        return root
    
h = MaxHeap()

h.insert(3)
h.insert(1)
h.insert(5)

print("Heap:", h.h)
print("Delete:", h.delete())
print("After delete:", h.h)

#Heap operations
class Heap:
    def __init__(self):
        self.h = []

    # INSERT
    def insert(self, x):
        self.h.append(x)
        i = len(self.h) - 1
        while i > 0 and self.h[(i-1)//2] > self.h[i]:
            self.h[i], self.h[(i-1)//2] = self.h[(i-1)//2], self.h[i]
            i = (i-1)//2

    # HEAPIFY (down)
    def heapify(self, i):
        smallest = i
        l = 2*i + 1
        r = 2*i + 2

        if l < len(self.h) and self.h[l] < self.h[smallest]:
            smallest = l
        if r < len(self.h) and self.h[r] < self.h[smallest]:
            smallest = r

        if smallest != i:
            self.h[i], self.h[smallest] = self.h[smallest], self.h[i]
            self.heapify(smallest)

    # DELETE (extract min)
    def delete(self):
        if len(self.h) == 0:
            return None
        root = self.h[0]
        self.h[0] = self.h[-1]
        self.h.pop()
        self.heapify(0)
        return root


# 🔹 FUNCTION CALL
h = Heap()

h.insert(4)
h.insert(1)
h.insert(3)

print("Heap:", h.h)
print("Deleted:", h.delete())
print("After delete:", h.h)

#Tree view
h = [1,3,5]

# Delete (extract min)
heapq.heappop(h)

print(h)
#BFS 
from collections import deque

def bfs_shortest(graph, start, goal):
    q = deque([(start, [start])])   # (node, path)
    visited = set([start])

    while q:
        node, path = q.popleft()

        if node == goal:
            return path

        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                q.append((n, path + [n]))

# Function Call
g = {1:[2,3], 2:[4], 3:[4], 4:[]}
print(bfs_shortest(g, 1, 4))


#Tree view
from collections import deque

def bfs(g, start):
    q = deque([start])
    vis = set([start])

    while q:
        node = q.popleft()
        print(node, end=" ")
        for n in g[node]:
            if n not in vis:
                vis.add(n)
                q.append(n)

g = {1:[2,3], 2:[4], 3:[], 4:[]}
bfs(g, 1)
#infix to postfix

def prec(op):
    if op in "+-": return 1
    if op in "*/": return 2
    return 0

def infix_to_postfix(exp):
    stack = []
    res = ""

    for ch in exp:
        if ch.isalnum():
            res += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack[-1] != '(':
                res += stack.pop()
            stack.pop()
        else:
            while stack and prec(ch) <= prec(stack[-1]):
                res += stack.pop()
            stack.append(ch)

    while stack:
        res += stack.pop()

    return res

# Function Call
print(infix_to_postfix("A+B*C"))

#dfs 

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for n in graph[node]:
            dfs(graph, n, visited)

# Function Call
g = {1:[2,3], 2:[4], 3:[], 4:[]}
dfs(g, 1, set())

#tree view
def dfs(g, node, vis):
    if node not in vis:
        print(node, end=" ")
        vis.add(node)
        for n in g[node]:
            dfs(g, n, vis)


g = {1:[2,3], 2:[4], 3:[], 4:[]}

dfs(g, 1, set())