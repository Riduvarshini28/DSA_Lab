class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# INSERT
def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root

# INORDER (prints sorted)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# SEARCH
def search(root, x):
    if root is None or root.data == x:
        return root
    if x < root.data:
        return search(root.left, x)
    return search(root.right, x)


# 🔹 FUNCTION CALL

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)

print("Inorder:")
inorder(root)

print("\nSearch 40:", search(root, 40) is not None)





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