# https://leetcode.com/problems/unique-paths/

from pprint import pprint


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * (m + 1) for _ in range(n + 1)]

        pprint(dp)
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                print(i, j, dp[i][j])
                pprint(dp)

        pprint(dp)
        return dp[n-1][m-1]

sl = Solution()
m = 7
n = 3
print(sl.uniquePaths(m, n))
