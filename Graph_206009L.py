
class Graph:
    # Initialize the matrix
    def __init__(self, size):
        self.matrix = []
        for i in range(size):
            self.matrix.append([0] * size)
            self.size = size

    # Add edges
    def addEdge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1
    
    # Check whether (u,v) is an edge
    def isEdge(self, u, v):
        if self.matrix[u][v] == 1:
            print("An edge exists between %d and %d" % (u, v))
            return
        else:
            print("No edge between %d and %d" % (u, v))
            return
    
    def BFS(self, x):
        visited = [False] * self.size
        queue = [x]
        visited[x] = True
 
        while queue:
            vis = queue[0]
            print(vis, end = ' ')
            queue.pop(0)
            for i in range(self.size):
                if (self.matrix[vis][i] == 1 and
                      (not visited[i])):
                    queue.append(i)
                    visited[i] = True
    
    def DFS(self, x):
        stack = []
        visited = [False] * self.size
        visited[x] = True
        stack.append(x)
        print(x, end = " ")
        for i in range(x+1):
            if (self.matrix[x][i] == 1 and
                    (not visited[i])):
                self.DFS(i)


# Creating a graph with a matrix structure of size 6
g = Graph(6)

# Adding edges to the graph
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(5, 3)
g.addEdge(2, 5)
g.addEdge(4, 5)
g.addEdge(1, 5)


# Checking whether edge exists
g.isEdge(2,5)
g.isEdge(0,5)


# Performing a BFS for 5
g.BFS(5)


# Performing a DFS for 3
g.DFS(3)