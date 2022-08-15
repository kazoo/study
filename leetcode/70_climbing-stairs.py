# https://leetcode.com/problems/climbing-stairs/

# 一応再起処理の上限を増やしたい時は
# import sys
# sys.setrecursionlimit(2000)
# で、できる。デフォルトは1000
class Solution:

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        two_steps_before = 1
        one_step_before = 2
        ans = 0

        for i in range(2, n):
            ans = two_steps_before + one_step_before
            two_steps_before = one_step_before
            one_step_before = ans
        return ans

    # leetcode では maximum recursion depth exceeded
    def climbStairs2(self, n: int) -> int:
        memo = {}

        def step(n):
            if n <= 2:
                return n
            if n in memo:
                return memo[n]

            memo[n] = step(n-1) + step(n-2)

            return memo[n]
        return step(n)


sl = Solution()
n = 40
print(sl.climbStairs(n))
