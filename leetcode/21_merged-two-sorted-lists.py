# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        if p1 == None:
            return p2
        elif p2 == None:
            return p1
        current = list1
        if p1.val <= p2.val:
            current = list1
            p1 = p1.next
        else:
            current = list2
            p2 = p2.next
        top = current
        
        while p1 != None and p2 != None:
#            print(p1.val, p2.val)
            if p1.val <= p2.val:
                current.next = p1
                current = current.next
                p1 = p1.next
            else:
                current.next = p2
                current = current.next
                p2 = p2.next
                
        if p1:
            current.next = p1
        else:
            current.next = p2
        return top        


def createNode(l):
    next = None
    for i in range(len(l)):
        ll = ListNode(l[-1 - i], next)
        next = ll
    return ll

l1 = [1,2,4]
l2 = [1,3,4]
node1 = createNode(l1)
node2 = createNode(l2)

sl = Solution()
print(sl.mergeTwoLists(node1, node2))
