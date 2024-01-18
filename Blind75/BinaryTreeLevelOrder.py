from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: [TreeNode]) -> [[int]]:

        if root is None:
            return []

        levels_node_map = defaultdict(list)

        queue = [(root, 0)]  # level for root is 0

        while queue:
            node, level = queue.pop(0)

            levels_node_map[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        result = []
        for i in range(len(levels_node_map)):
            result.append(levels_node_map[i])

        return result
