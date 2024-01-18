import collections

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = collections.defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive dfs function used by topologicalSort
    # to run a Depth first traversal starting from a given node/vertex
    def dfsUtil(self, v, visited, ordering):

        # Mark the current node as visited.
        visited[v] = True

        # Recurse for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.dfsUtil(i, visited, ordering)

        # Push current vertex to ordering which stores result
        ordering.insert(0, v)

    # The function to do Topological Sort. It uses recursive
    # DfsUtil on all vertices that have not been visited
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        ordering = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if not visited[i]:
                self.dfsUtil(i, visited, ordering)

        # Print contents of the ordering
        print(ordering)


# Run test
graph = Graph(6)
graph.addEdge(5, 2)
graph.addEdge(5, 0)
graph.addEdge(4, 0)
graph.addEdge(4, 1)
graph.addEdge(2, 3)
graph.addEdge(3, 1)

print("Valid Topological Ordering for the Graph --->")
graph.topologicalSort()
