# https://leetcode.com/problems/merge-two-binary-trees/

import collections
from pprint import pprint
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else:
            return root1 or root2


def createTree(list):
    n = len(list)
    if n == 0:
        return []
    
    root = TreeNode(list[0])
    def addNode(node, idx):
        if idx * 2 - 1 < n and list[idx * 2 - 1]:
            node.left = TreeNode(list[idx * 2 - 1])
            addNode(node.left, idx * 2)
        if idx * 2 < n and list[idx * 2]:
            node.right = TreeNode(list[idx * 2])
            addNode(node.right, idx * 2 + 1)
    
    addNode(root, 1)
    return root


def print_bfs(root):
    q = deque([root])
    ans = []

    def left2right(q):
        l = len(q)
        layer_val = []
        for _ in range(l):
            node = q.popleft()
            print(node.val if node else 'None')
            layer_val.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(layer_val)
        if len(q) > 0:
            left2right(q)
    left2right(q)
    return ans

sl = Solution()
root1 = [1,3,2,5]
root2 = [2,1,3,None,4,None,7]

tree1 = createTree(root1)
print("---")
print_bfs(tree1)
tree2 = createTree(root2)
print("---")
print_bfs(tree2)
merged = sl.mergeTrees(tree1, tree2)
print("---")
print_bfs(merged)