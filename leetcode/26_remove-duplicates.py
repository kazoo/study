# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = []
        i = 0
        while i < len(nums):
            if nums[i] in visited:
                nums = nums[:i] + nums[i+1:]
            else:
                visited.append(nums[i])
                i += 1
        print(nums)
        return len(nums)
    

sl = Solution()
nums = [1,1,2]
print(sl.removeDuplicates(nums))
