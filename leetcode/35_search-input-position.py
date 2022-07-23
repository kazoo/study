# https://leetcode.com/problems/search-insert-position/

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        head = 0
        tail = l
        while head <= tail:
            print(head, tail)
            if head == tail:
                if head == l or nums[head] >= target:
                    return head
                else:
                    return head - 1

            c = int((head + tail) / 2)
            if nums[c] < target:
                head = c + 1
            else:
                tail = c

        return -1


l = [1,3,5,6]
target = 7
s = Solution()
print(s.searchInsert(l, target))
