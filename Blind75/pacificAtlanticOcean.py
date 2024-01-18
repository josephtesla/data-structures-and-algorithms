"""
Time --> O(NXM)
"""

class Solution:
    def pacificAtlantic(self, heights: [[int]]) -> [[int]]:
        rows, cols = len(heights), len(heights[0])
        atlantic_set, pacific_set = set(), set()
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs_helper(r, c, visit_set):
            if (r, c) in visit_set:
                return

            visit_set.add((r, c))
            for direction in moves:
                next_r, next_c = r + direction[0], c + direction[1]
                if 0 <= next_c < cols and 0 <= next_r < rows and heights[r][c] <= heights[next_r][next_c]:
                    dfs_helper(next_r, next_c, visit_set)

        # check the column atlantic and pacific edges and mark cells that can reach them
        for r in range(rows):
            # for pacific ocean
            dfs_helper(r, 0, pacific_set)
            # for atlantic ocean
            dfs_helper(r, cols - 1, atlantic_set)

        # check the row atlantic and pacific edges and mark cells that can reach them
        for c in range(cols):
            # for pacific ocean
            dfs_helper(0, c, pacific_set)
            # for atlantic ocean
            dfs_helper(rows - 1, c, atlantic_set)

        results = []
        for r in range(rows):
            for c in range(cols):
                # if the cell can be reached from both atlantic and pacific oceans
                if (r, c) in atlantic_set and (r, c) in pacific_set:
                    results.append([r, c])

        return results


print(Solution().pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
