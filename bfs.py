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