from collections import defaultdict


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = [False] * n
        recur_stack = [False] * n

        def dfs_cycle_exists(node, parent_from=float("-inf")):
            visited[node] = True
            recur_stack[node] = True

            for adj in graph[node]:
                if not visited[adj]:
                    if dfs_cycle_exists(adj, node):
                        return True

                if recur_stack[adj] and adj != parent_from:
                    return True

            recur_stack[node] = False
            return False

        for i in range(n):
            if n > 1 and len(graph[i]) == 0:
                return False

            if not visited[i] and dfs_cycle_exists(i):
                return False

        return True


# Complete the 'sExpression' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING nodes as parameter.
#
from collections import defaultdict

print(min("A", "B"))


def sExpression(nodes):
    # Write your code here
    graph = defaultdict(list)
    root = None
    for pair in nodes.split(" "):
        c1, c2 = pair[1], pair[3]

        if not root:
            root = min(c1, c2)
        else:
            root = min(c1, c2, root)

        graph[c1].append(c2)
        graph[c2].append(c1)
        if len(graph[c1]) > 2 or len(graph[c2]) > 2:
            return "E1"

        if len(graph[c1]) == 2:
            if graph[c1][0] == graph[c1][1]:
                return "E2"

        if len(graph[c2]) == 2:
            if graph[c2][0] == graph[c2][1]:
                return "E2"

    _visited = set()
    recur_stack = set()

    def cycleExists(node, parent=None):
        _visited.add(node)
        recur_stack.add(node)
        for adj in graph[node]:
            if adj not in _visited:
                if cycleExists(adj, node):
                    return True

            if adj in recur_stack and parent != adj:
                return True

        recur_stack.remove(node)
        return False

    print(graph)
    if cycleExists("A"):
        return "E3"

    for node in list(graph.keys()):
        if not node in _visited:
            return "E4"

    return "ok"


if __name__ == '__main__':
    print(sExpression("(A,B) (B,D) (A,C) (D,C)"))