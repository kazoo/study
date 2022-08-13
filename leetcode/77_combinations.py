# https://leetcode.com/problems/combinations/

import itertools
from typing import List

class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [n for n in range(1, n+1)]

        def comb(nums, r):
            if r == 1:
                return [[k] for k in nums]

            result = []
            for i,val in enumerate(nums):
                rest = comb(nums[i+1:], r - 1)
                for _ in rest:
                    result.append([val] + _)
            return result
        return comb(nums, k)

    # Yes
    def combine2(self, n: int, k: int) -> List[List[int]]:
        return itertools.combinations([n for n in range(1, n+1)], k)

sl = Solution()
print(sl.combine(4, 2))
