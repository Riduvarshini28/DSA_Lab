class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def insert(self, x):
        new = Node(x)
        if self.head:
            self.head.prev = new
            new.next = self.head
        self.head = new

    def print_list(self):
        t = self.head
        while t:
            print(t.data, end=" <-> ")
            t = t.next

# Function Call
d = DLL()
d.insert(10)
d.insert(20)
d.insert(30)
d.print_list()