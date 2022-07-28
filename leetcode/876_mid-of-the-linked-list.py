# https://leetcode.com/problems/middle-of-the-linked-list/


# Definition for singly-linked list.
import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # slow and fast pointer
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast:
            if fast.next == None:
                return slow
            slow = slow.next
            fast = fast.next.next

        

    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        current = head
        while current:
            cnt += 1
            current = current.next
        
        current = head
        for _ in range(int(cnt/2)):
            current = current.next

        return current

l = [0,1,2,3,4,5]
next = None
for i in range(len(l)):
    ll = ListNode(l[-1-i], next)
    next = ll

sl = Solution()
mid = sl.middleNode(ll)
while mid:
    print(mid.val)
    mid = mid.next


