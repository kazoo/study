# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = len(s)
    
        for i in range(int(l/2)):
            if s[i] != s[-1 - i]:
                return False
        return True

s = Solution()
x = -1234321
print(s.isPalindrome(x))
