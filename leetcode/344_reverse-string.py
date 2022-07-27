# https://leetcode.com/problems/reverse-string/

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(int(l/2)):
            s[i], s[-1-i] = s[-1-i], s[i]
        
        print(s)

s = Solution()
st = ["h", "e", "l", "l", "o"]
s.reverseString(st)
