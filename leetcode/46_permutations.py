# https://leetcode.com/problems/permutations/

from typing import List
import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        l = len(nums)

        def perm(head):
            if len(head) == 1:
                return head
            res = []
            for i, val in enumerate(head):
                rest = perm(nums[:i] + nums[i+1:])
                for _ in rest:
                    res.append([val] + _)
            return res

        print(perm(nums))
        return ans

    def power(self, n) -> int:
        if n <= 1:
            return n
        return n * self.power(n-1)


sl = Solution()
print(sl.permute([1,2,3]))
