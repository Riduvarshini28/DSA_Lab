
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