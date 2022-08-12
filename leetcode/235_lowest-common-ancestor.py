# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root

        current = root
        while current:
            if min(p.val, q.val) <= current.val <= max(p.val, q.val):
                return current
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                current = current.right
