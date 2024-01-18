"""
Time complexity
M * N * 4^S
where S is the length of the string
"""

class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def search(i, j, word, idx, visited):
            if (i, j) in visited:
                return False

            if board[i][j] != word[idx]:
                return False

            if idx == len(word) - 1 and board[i][j] == word[idx]:
                return True

            visited.add((i, j))
            for r, c in moves:
                next_i, next_j = i + r, j + c
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if search(next_i, next_j, word, idx + 1, visited):
                        visited.remove((i, j))
                        return True

            visited.remove((i, j))
            return False

        visited = set()
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if search(i, j, word, 0, visited):
                        return True

        return False
