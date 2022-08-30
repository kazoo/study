# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        # NG: 2, 3, 4, 5, 6, 8, 9
        # OK: 1, 7

        while n >= 10:
            s = str(n)
            n = 0
            for _ in s:
                n += (int(_)) ** 2

        if n in [1, 7]:
            return True
        else:
            return False

sl = Solution()
print(sl.isHappy(2))
