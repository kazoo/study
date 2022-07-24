# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List

class Solution:

    # slow but less memory usage
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        l = len(nums)
        head = 0
        tail = l - 1
        while head <= tail:
            if nums[head] ** 2 < nums[tail] ** 2:
                ans.insert(0, nums[tail] ** 2)
                tail -= 1
            else:
                ans.insert(0, nums[head] ** 2)
                head += 1
        return ans


    # std lib is ok
    def sortedSquares2(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            print(n ** 2)
            ans.append(n ** 2)

        return sorted(ans)

s = Solution()
l = [-4,-1,0,3,10]
print(s.sortedSquares(l))