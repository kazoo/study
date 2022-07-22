# https://leetcode.com/problems/partition-list/

from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        current = head
        f_half = None
        s_half = None
        s_half_top = None

        while current != None:
            if current.val < x:
                if f_half == None:
                    f_half = current
                    f_half_top = current
                else:
                    f_half.next = current
                    f_half = f_half.next
            else:
                if s_half == None:
                    s_half = current
                    s_half_top = current
                else:
                    s_half.next = current
                    s_half = s_half.next
            current = current.next

        if f_half == None:
            s_half.next = None
            return s_half_top
        elif s_half == None:
            f_half.next = None
        else:
            f_half.next = s_half_top
            s_half.next = None
#        self.dump(head, 6)
        return f_half_top

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
li = [1,4,3,2,5,2]
# li = [2,1]
l = len(li)
lnode = None
for i in range(l):
    lnode = ListNode(li[l-i-1], lnode)

# print(s.simpleReverse(lnode))
pp = s.partition(lnode, 3)
s.dump(pp, 6)
