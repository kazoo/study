# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(0, x+1):
            if i * i == x:
                return i
            if i * i > x:
                return i - 1

x = 4
s = Solution()
print(s.mySqrt(x))
