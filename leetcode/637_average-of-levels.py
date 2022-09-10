# https://leetcode.com/problems/average-of-levels-in-binary-tree/


from collections import deque
import decimal
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
#        decimal.getcontext().prec = 7
        ans = []
        nodes = []

        q = deque([(0, root)])
        while q:
            (l, n) = q.popleft()
            if len(ans) == l:
                ans.append(decimal.Decimal(n.val))
                nodes.append(1)
            else:
                ans[l] += n.val
                nodes[l] += 1
            if n.left:
                q.append((l + 1, n.left))
            if n.right:
                q.append((l + 1, n.right))

        for i in range(len(ans)):
            ans[i] = round(ans[i] / nodes[i], 5)
        return ans
