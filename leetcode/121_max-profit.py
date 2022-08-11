# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = prices[0]
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            profit = max(prices[i] - min, profit)

        return profit

sl = Solution()
prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
print(sl.maxProfit(prices))
