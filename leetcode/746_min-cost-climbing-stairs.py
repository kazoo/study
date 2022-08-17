# https://leetcode.com/problems/min-cost-climbing-stairs/

from asyncio import constants
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        # dp[i]: i段目までの最小コスト
        dp = [0] * (l+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        # 階段を登り切るので最後にコスト0の段を追加
        cost.append(0)

        for i in range(2, l+1):
            if dp[i-1] < dp[i-2]:
                dp[i] = dp[i-1] + cost[i]
            else:
                dp[i] = dp[i-2] + cost[i]
        return dp[l]

sl = Solution()
costs = [10,15,20]
costs = [1,100,1,1,1,100,1,1,100,1]
print(sl.minCostClimbingStairs(costs))
