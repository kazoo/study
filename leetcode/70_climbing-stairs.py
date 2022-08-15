# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        return self.climbStairs(n-1) + self.climbStairs(n-2)


sl = Solution()
n = 40
print(sl.climbStairs(n))
