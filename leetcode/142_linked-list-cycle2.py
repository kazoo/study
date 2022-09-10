# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current:
            if current.val == None:
                return current

            if current.next == None:
                return None

            current.val = None
            current = current.next
