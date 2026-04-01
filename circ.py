class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class CLL:
    def __init__(self):
        self.tail = None

    def insert(self, x):
        new = Node(x)
        if not self.tail:
            self.tail = new
            new.next = new
        else:
            new.next = self.tail.next
            self.tail.next = new
            self.tail = new

    def print_list(self):
        if not self.tail:
            return
        t = self.tail.next
        while True:
            print(t.data, end=" ")
            t = t.next
            if t == self.tail.next:
                break

# Function Call
c = CLL()
c.insert(10)
c.insert(20)
c.insert(30)
c.print_list()