# https://leetcode.com/problems/coin-change-2/description/

from collections import deque
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
               if j >= i:
                   dp[j] += dp[j - i]
        return dp[amount]

    # WA...
    def change2(self, amount: int, coins: List[int]) -> int:
        ans = 0
        q = deque(coins)

        while q:
            print(q)
            n = q.popleft()
            for c in coins:
                if n + c == amount:
                    ans += 1
                elif n + c + min(coins) <= amount:
                    q.append(n + c)

        return ans

sl = Solution()
coins = [1,2,5]
amount = 5
print(sl.change(amount, coins))
