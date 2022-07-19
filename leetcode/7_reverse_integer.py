# https://leetcode.com/problems/reverse-integer/
 
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        st = str(x)
        is_minus = st[0] == '-'
        if is_minus:
            st = st[1:]

        while st[-1] == '0':
            st = st[:-1]

        l = len(st)
        ans = 0
        for i in range(l):
            ans += int(st[-1-i]) * 10 ** (l - i - 1)

        if ans < -2 ** 31 or ans > 2 ** 31 - 1:
            return 0
        
        return ans * (-1 if is_minus else 1)

s = Solution()
x = 1534236469
print(s.reverse(x))

