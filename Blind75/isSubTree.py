# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def same_tree(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val == q.val:
            return self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)

        return False

    def isSubtree(self, root: [TreeNode], subRoot: [TreeNode]) -> bool:
        if root is None:
            if subRoot is None:
                return True
            else:
                return False

        if self.same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
