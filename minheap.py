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