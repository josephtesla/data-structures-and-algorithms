# Definition for a binary tree node.
class TreeNode:

    # Time Complexity -->O(n)

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def checkValid(node, left_boundary, right_boundary):
            if node is None:
                return True

            if not (left_boundary < node.val < right_boundary):
                return False

            return (checkValid(node.left, left_boundary, node.val)
                    and checkValid(node.right, node.val, right_boundary))

        return checkValid(root, float("-inf"), float("inf"))
