# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    # 再帰で後ろからインデックスしてi>nを全部ずらす
    def removeNthFromEnd3(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next

    # ???
    def removeNthFromEnd2(self, head, n):
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]

    # fast and slow pointer
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    def removeNthFromEnd4(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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

