# https://leetcode.com/problems/coin-change-2/description/

from collections import deque
from typing import List


class Solution:

    # dp[i][j] : i番目までの種類のコインで amount:j を作成できる組み合わせの数
    # 状態遷移は
    #
    # 1. i番目のコインを使わない → i-1番目までで j を作る → dp[i-1][j]
    # 2. i番目のコインを使う → 同じ種類のコインを何個使っても良いので、
    #    (i番目も使って）何通りで `j - coins[i-1]` を作れるかを調べる
    #    → すなわち、dp[i][j-coins[i-1]]
    #
    # dp[i][0] = 1 で初期化
    #
    # ここまでわかれば
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount + 1)]] * (len(coins) + 1)
        dp[0][0] = 1

        for i in range(1, len(coins)):
            dp[i][0] = 1
            for j in range(1, amount):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(coins)][amount]

    # さらに
    # dp[i][j] は、dp[i-1][j] と dp[i][j-coins[i]] のみに依存しているので、
    # 1次元配列に最適化できる
    def change2(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
               if j >= i:
                   dp[j] += dp[j - i]
        return dp[amount]

    # WA...
    def change3(self, amount: int, coins: List[int]) -> int:
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
