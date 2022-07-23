# https://leetcode.com/problems/binary-search/submissions/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        head = 0
        tail = l - 1
        while head <= tail:
            if tail == head:
                return head if nums[head] == target else -1
            c = int((tail + head)/2) + 1
            if nums[c] == target:
                return c
            elif nums[c] < target:
                head = c + 1
            else:
                tail = c - 1
#            print(head, tail)
        return -1

s = Solution()
nums = [2, 5]
target = 5
print(s.search(nums, target))