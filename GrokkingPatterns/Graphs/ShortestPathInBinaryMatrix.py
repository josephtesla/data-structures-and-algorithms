from collections import deque

class Solution:
    # Simple BFS algorithm
    def is_valid_cell(self, i, j, n, grid, visited):
        return (0 <= i < n) and (0 <= j < n) and grid[i][j] != 1 and not visited[i][j]

    def shortestPathBinaryMatrix(self, grid: [[int]]) -> int:
        n = len(grid)
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        visited = [[False] * n for i in range(n)]

        src, dest = (0, 0), (n - 1, n - 1)
        queue = deque()

        if grid[src[0]][src[1]] != 1:
            queue.append((src[0], src[1], 1))  # i, j, nodes distance from source

        while queue:
            i, j, distance = queue.popleft()
            if (i, j) == dest:
                return distance

            for move_x, move_y in moves:
                next_i, next_j = i + move_y, j + move_x
                if self.is_valid_cell(next_i, next_j, n, grid, visited):
                    queue.append((next_i, next_j, distance + 1))
                    visited[next_i][next_j] = True

        return -1




