# https://leetcode.com/problems/remove-element/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
#        nums = list(filter(lambda x:x != val, nums))
#        return len(nums)

        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
            else:
                nums[i] = '_'
        return i

sl = Solution()
nums = [3,2,2,3]
v = 3
print(sl.removeElement(nums, v))
