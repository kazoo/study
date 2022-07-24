# https://leetcode.com/problems/rotate-array/

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        tmp = nums[l-k:]
        tmp += nums[:l-k]
        for i in range(l):
            nums[i] = tmp[i]
        
#        print(nums)

s = Solution()
l = [1,2,3,4,5,6,7]
k = 1
s.rotate(l, k)
