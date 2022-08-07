# https://leetcode.com/problems/combination-sum-iv/

from collections import deque
from typing import List

class Solution:
    # with DP
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        print(dp[0], dp[1])
        for i in range(1, target + 1):
            for n in nums:
                if i >= n:
                    dp[i] += dp[i - n]
        print(dp)
        return dp[target]

    #
    def combinationSum3(self, nums: List[int], target: int) -> int:
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  > i: break
                if num == i: combs[i] += 1
                if num  < i: combs[i] += combs[i - num]
        return combs[target]

    # TLE
    def combinationSum(self, nums: List[int], target: int) -> int:
        self.ans = 0
        q = deque() # for debug dump

        # リストでなく合計を渡して n == target をチェックするだけでもOK
        def dfs(n, level):
            if level == 1:
                if sum(n) == target:
                    self.ans += 1
                    q.append(n)
                return n

            for _ in nums:
                if sum(n) + _ <= target:
                    dfs(n + [_], level - 1)


        for i in range(1, target + 1):
            if i == 1 and target in nums:
                q.append([target])
                self.ans += 1
                continue
            if i == target:
                if 1 in nums:
                    q.append([1 for _ in range(target)])
                    self.ans += 1
                break
            for _ in nums:
                if _ <= target:
                    dfs([_], i)
        print(q)
        return self.ans

sl = Solution()
# nums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# target = 10
nums = [1,50]
target = 200
print(sl.combinationSum3(nums, target))
print(sl.combinationSum4(nums, target))
