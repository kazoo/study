# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        cnt = 0
        lp = []
        while current:
            lp.append(current)
            current = current.next
            cnt += 1
        
        if cnt == 1:
            return ListNode("")
        elif cnt - n < 1:
            return lp[1]
        elif n == 1:
            lp[-2].next = None
        else:
            lp[-1-n].next = lp[-1-n+2]
        return head

l = [0,1,2,3,4,5]
next = None
for i in range(len(l)):
    ll = ListNode(l[-1-i], next)
    next = ll

sl = Solution()
lll = sl.removeNthFromEnd(ll, 6)
while lll:
    print(lll.val)
    lll = lll.next

