# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

class Solution:
    
    # brute force
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]

        # countしてそれを足した方が実際速い
        # cnt = nums.count(target)
        l = len(nums)
        s = 0
        e = l - 1
        found = False
        for i in range(l):
            if not found and nums[i] == target:
                found = True
                s = i
            elif found and nums[i] != target:
                e = i - 1
                break
        return [s, e]


    # binary search...?
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        cnt = nums.count(target)
        l = len(nums)
        
        head = c = 0
        tail = l
        while head < tail:
            c = int((tail + head) / 2)
            if nums[c] < target:
                head = c
            elif nums[c] > target:
                tail = c
            else:
                break
        
        i = 0
        while(c - i >= 0 and nums[c - i] == target):
            i += 1
        print(i)
        return [max(c - i + 1, 0), max(c - i + 1, 0) + cnt - 1]

s = Solution()
l = [5,7,7,8,8,10]
target = 10
print(s.searchRange(l, target))
        