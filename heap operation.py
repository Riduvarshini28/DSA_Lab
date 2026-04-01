#Heap operations
import heapq


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