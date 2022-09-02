# https://leetcode.com/problems/same-tree/submissions/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q  # <- return True if p==None and q==None else False

    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None:
            return True if q == None else False
        if q == None:
            return True if p == None else False

        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            if len(q1) != len(q2):
                return False
            n1 = q1.popleft()
            n2 = q2.popleft()

            if n1.val != n2.val:
                return False
            if n1.left:
                if n2.left == None:
                    return False
                q1.append(n1.left)
                q2.append(n2.left)
            else:
                if n2.left:
                    return False

            if n1.right:
                if n2.right == None:
                    return False
                q1.append(n1.right)
                q2.append(n2.right)
            else:
                if n2.right:
                    return False
        return True
