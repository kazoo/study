# https://leetcode.com/problems/longest-common-prefix/

from re import S
from typing import List

class Solution:
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            if prefix == "":
                break
            j = 0
            while j <= len(strs[i]) and j < len(prefix):
                if j == len(strs[i]) or strs[i][j] != prefix[j]:
                    prefix = prefix[:j]
                    break
                j += 1
        return prefix

    # 先に最短をprefixにするとスマート & pythonic!
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 組み込み関数をkeyに指定できる。
        # max(nums, key=abs)
        # sorted(strs, key=len)
        # といったものも
        shortest = min(strs,key=len)

        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

sl = Solution()
strs = ["dog","racecar","car"]
strs = ["aaa","aa","aaa"]
print(sl.longestCommonPrefix(strs))
