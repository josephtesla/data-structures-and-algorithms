class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(i, j):
            if (i, j) in visited:
                return

            visited.add((i, j))
            for move in moves:
                next_i, next_j = i + move[0], j + move[1]
                if 0 <= next_i < rows and 0 <= next_j < cols and grid[next_i][next_j] == "1":
                    dfs(next_i, next_j)

        island_count = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    island_count += 1

        return island_count


print(Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))