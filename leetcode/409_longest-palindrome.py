# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = {}
        for _ in s:
            if _ not in c:
                c[_] = 1
            else:
                c[_] += 1
        count = 0
        odd = False
        for key in c:
            q, mod = divmod(c[key], 2)
            count += q * 2
            if not odd and mod > 0:
                odd = True
        return count + (1 if odd else 0)

sl = Solution()
s = "bb"
print(sl.longestPalindrome(s))
