# https://qiita.com/drken/items/a5e6fe22863b7992efdb

from pprint import pprint
from typing import List

# 重さwを超えないようにナップサックの価値vを最大化する
class Solution:
    def getMaxValue(self, items: List[List[int]], weight: int) -> int:
        # dp[i][w]: 重さwを超えないように、i-1までのアイテムで選んだ価値の最大値

        li = len(items)
        lv = 100 # len(items) * len(items[0]) * 10
        dp = [[0] * (lv + 1) for _ in range(li + 1)]

        pprint(dp)
        for i in range(li):
            for j in range(lv):
                if j >= items[i][1]:
                    # 入れる場合と入れない場合で価値が大きい方を選ぶ
                    dp[i+1][j] = max(dp[i][j], dp[i][j - items[i][0]] + items[i][1])
                else:
                    # もう入れられない
                    dp[i+1][j] = dp[i][j]

        return dp[li][weight]

s = Solution()
# (weight, value)
items = [[2, 3], [1, 2], [3, 6], [2, 1], [1, 3], [5, 85]]
w = 9
print(s.getMaxValue(items, 9))
