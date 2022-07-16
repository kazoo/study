# https://leetcode.com/problems/add-two-numbers/

import math
from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = l1
        ln1 = 0
        digit = 0
        while current:
            ln1 += current.val * 10 ** digit
            digit += 1
            current = current.next

        current = l2
        ln2 = 0
        digit = 0
        while current:
            ln2 += current.val * 10 ** digit
            digit += 1
            current = current.next

        nl = None
        for _ in str(ln1 + ln2):
            nl = ListNode(_, nl)

        return nl


    def listNodeFromList(self, n: List[int]):
        ln = None
        for i in range(len(n)):
            ln = ListNode(n[-1-i], ln)
        return ln

s = Solution()
l1 = s.listNodeFromList([2,4,3])
l2 = s.listNodeFromList([5,6,4])

ln = s.addTwoNumbers(l1, l2)
while ln:
    print(ln.val)
    ln = ln.next


