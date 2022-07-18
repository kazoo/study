
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

from functools import reduce
from typing import List

class Solution:
    def join(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        ret = 0
#        for _ in nums:
#            ret += _
#        return ret
        return reduce(lambda x,y: x+y, nums)

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = self.join(cardPoints)
        remaining_length = len(cardPoints) - k
        remaining = self.join(cardPoints[:remaining_length])
        ans = total - remaining
        for i in range(0, len(cardPoints) - remaining_length):
            remaining += cardPoints[i+remaining_length]
            remaining -= cardPoints[i]
            ans = max(ans, total - remaining)
        return ans

    # TLE
    def maxScore2(self, cardPoints: List[int], k: int) -> int:
        ans = 0
        for i in range(k+1):
            heads = cardPoints[:i]
            if i == k:
                tails = []
            else:
                tails = cardPoints[i-k:]
            ans = max(ans, self.join(heads) + self.join(tails))
        return ans
    

# cardPoints = [96,90,41,82,39,74,64,50,30]
# k = 8
cardPoints = [1,79,80,1,1,1,200,1]
k = 3
s = Solution()
print(s.maxScore(cardPoints, k))
