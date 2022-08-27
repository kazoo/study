# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseqs = [[nums[0]]]
        minimum = nums[0]

        for i in range(1, len(nums)):
            print(subseqs)
            for s in subseqs:
                if s[-1] < nums[i]:
                    s.append(nums[i])
            if minimum >= nums[i]:
                subseqs.append([nums[i]])

        return max(map(len, subseqs))

sl = Solution()
nums = [0,1,0,3,2,3]
print(sl.lengthOfLIS(nums))
