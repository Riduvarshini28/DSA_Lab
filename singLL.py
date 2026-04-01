class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def print_list(self):
        t = self.head
        while t:
            print(t.data, end=" -> ")
            t = t.next

# Function Call
l = SLL()
l.insert(10)
l.insert(20)
l.insert(30)
l.print_list()