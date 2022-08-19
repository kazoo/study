# https://leetcode.com/problems/backspace-string-compare/

from collections import deque


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sq = deque()
        tq = deque()
        for _ in s:
            if _ == '#':
                if sq: sq.pop()
            else:
                sq.append(_)
        for _ in t:
            if _ == '#':
                if tq: tq.pop()
            else:
                tq.append(_)
        return sq == tq

sl = Solution()
s = "y#fo##f"
t = "y#f#o##f"
s = "ab#c"
t = "ad#c"
print(sl.backspaceCompare(s, t))
