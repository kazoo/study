# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root

        ans = []
        q = collections.deque([root])
        idx = 0

        def helper(q, idx):
            l = len(q)
            next = None
            for _ in range(l):
                node = q.popleft()
                node.next = next
                ans.insert(idx, node)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                next = node
            if len(q) > 0:
                helper(q, len(ans))

        helper(q, 0)
        return ans[0]


