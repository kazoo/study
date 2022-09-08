# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(node):
            if node.left:
                inorder(node.left)
            ans.append(node.val)
            if node.right:
                inorder(node.right)

        if root:
            inorder(root)
        return ans

