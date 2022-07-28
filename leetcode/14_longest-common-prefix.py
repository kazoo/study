# https://leetcode.com/problems/longest-common-prefix/

from re import S
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            if prefix == "":
                break
            j = 0
            while j <= len(strs[i]) and j < len(prefix):
                print(i, j)
                if j == len(strs[i]) or strs[i][j] != prefix[j]:
                    prefix = prefix[:j]
                    break
                j += 1
        return prefix

sl = Solution()
strs = ["dog","racecar","car"]
strs = ["aaa","aa","aaa"]
print(sl.longestCommonPrefix(strs))
