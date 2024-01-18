class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word):
        current = self
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_word = True

"""
Time Complexity -->
M * N * 4^L
where L is the length of the longest string length
"""

class Solution:
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        root = TrieNode()
        for w in words:
            root.insert(w)

        rows, cols = len(board), len(board[0])
        visited = set()
        result = set()

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, trie_level, formed):
            if (i < 0 or j < 0 or i >= rows or
                    j >= cols or (i, j) in visited or
                    (board[i][j] not in trie_level.children)):
                return

            ch = board[i][j]
            next_level = trie_level.children[ch]
            formed += ch
            if next_level.is_word:
                result.add(formed)

            visited.add((i, j))
            for r, c in moves:
                next_i, next_j = i + r, j + c
                dfs(next_i, next_j, next_level, formed)

            visited.remove((i, j))

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, "")

        return list(result)
