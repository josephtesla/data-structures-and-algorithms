from collections import defaultdict

"""
O(N) Time complexity
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:

        # build graph
        graph = defaultdict(list)
        for [a, b] in prerequisites:
            graph[b].append(a)

        # detect a cycle in the graph
        visited = [False] * numCourses
        recursionStack = [False] * numCourses

        def cycleExists(node):
            visited[node] = True
            recursionStack[node] = True
            for adj in graph[node]:
                if visited[adj] is False:
                    if cycleExists(adj) is True:
                        return True

                if recursionStack[adj]:
                    return True

            recursionStack[node] = False
            return False

        for n in range(numCourses):
            if not visited[n]:
                if cycleExists(n) is True:
                    return False

        return True




