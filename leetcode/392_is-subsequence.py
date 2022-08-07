# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for _ in s:
            if _ in t:
                k = t.index(_)
                t = t[k+1:]
            else:
                return False
            
        return True
    