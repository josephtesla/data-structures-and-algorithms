from collections import defaultdict
"""
O(N) Complexity
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        # modify topological ordering. checking for cycle

        # build graph
        graph = defaultdict(list)
        for [a, b] in prerequisites:
            graph[b].append(a)

        # check cycle and record topological ordering
        print(graph)
        visited = [False] * numCourses
        in_recursion = [False] * numCourses
        ordering = []

        def topoCycleExists(node):
            visited[node] = True
            in_recursion[node] = True
            for adj in graph[node]:
                if not visited[adj]:
                    if topoCycleExists(adj):
                        return True

                if in_recursion[adj]:
                    return True

            ordering.insert(0, node)
            in_recursion[node] = False
            return False

        for course_node in range(numCourses):
            if not visited[course_node]:
                if topoCycleExists(course_node):
                    return []

        return ordering
