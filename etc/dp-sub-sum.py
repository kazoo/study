# https://qiita.com/drken/items/a5e6fe22863b7992efdb

from pprint import pprint
from typing import List

# リストの一部または全部を合計してtargetが作れるかどうか
class Solution:
    def canMakeTarget(self, nums: List, target: int) -> bool:
        # dp[i+1][w]: i番目までの数字から何個かを合計してtargetを作れるかどうか
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]

        # 初期条件：0個の整数の和は0なので、dp[0][0] のみ True にする
        dp[0][0] = True
        pprint(dp)

        for i in range(len(nums)):
            for j in range(target + 1):
                # nums[i+1]を足さない場合
                # dp[i][j] が True ならすでに target はできる
                dp[i+1][j] |= dp[i][j]

                # nums[i+1]を足す場合
                # (j>nums[i]のとき) dp[i][j-nums[i]] が True ならできる
                if j >= nums[i]:
                    dp[i+1][j] |= dp[i][j-nums[i]]

        pprint(dp)

        return dp[len(nums)][target]


s = Solution()
nums = [7, 5, 6, 5, 2]
target = 10
print(s.canMakeTarget(nums, target))

