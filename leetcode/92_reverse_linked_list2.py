# https://leetcode.com/problems/reverse-linked-list-ii/

import math
from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        current = head
        following = head
        previous = None
        idx = 1
        while current != None:
            if idx == left:
                edge_f = current
                edge_p = previous
                while idx <= right and current != None:
                    following = following.next
                    current.next = previous
                    previous = current          
                    current = following
                    idx += 1
                edge_f.next = current
                if edge_p != None:
                    edge_p.next = previous
                else:
                    head = previous
                continue

            following = following.next
            previous = current
            current = current.next
            idx += 1

        return head

    def simpleReverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        following = head
        previous = None
        while current != None:
            following = following.next
            current.next = previous
            previous = current
            current = following
        return previous

    # debug
    def dump(self, ln: ListNode, s:int):
        head = ln
        l = []
        i = 0
        while head != None and i < s:
            i += 1
            l.append(head.val)
            head = head.next
        print(l)

s = Solution()
li = [1,2,3,4,5]
# li = [3,5]
l = len(li)
lnode = None
for i in range(l):
    lnode = ListNode(li[l-i-1], lnode)

# print(s.simpleReverse(lnode))
print(s.reverseBetween(lnode, 1, 2))

