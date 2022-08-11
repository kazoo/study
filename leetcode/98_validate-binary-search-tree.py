# https://leetcode.com/problems/validate-binary-search-tree/

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # current = -2 ** 31
        # q = deque([root])
        # while q:
        #     edge = q.pop()
        #     print(edge.val)
        #     if edge.left != None:
        #         q.append(edge.left)
        #         continue
        #     print(edge.val)
        #     if edge.val <= current:
        #         return False
        #     current = edge.val
        #     if edge.right != None:
        #         q.append(edge.right)
        # return True

        self.ans = True
        self.current = -2 ** 31
        def dfs(edge):
            print(edge.val)
            if edge.left != None:
                dfs(edge.left)
            if edge.val <= self.current:
                self.ans = False
            self.current = edge.val

            if edge.right != None:
                dfs(edge.right)

        dfs(root)

        return self.ans

        # return dfs(root)


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
# root1 = [1,3,2,5]
# root2 = [2,1,3,None,4,None,7]
root = [5,1,4,None,None,3,6]

tree = createTree(root)
print(sl.isValidBST(tree))
