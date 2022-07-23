# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

from mimetypes import init


class Solution:

    def __init__(self, v: int):
        self.first_bad_version = v

    def isBadVersion(self, v: int):
        return v >= self.first_bad_version

    def firstBadVersion(self, n: int) -> int:
        head = 0
        tail = n
        while head <= tail:
            if tail == head:
                return head + 1
            c = int((head + tail) / 2) 
            if self.isBadVersion(c + 1):
                tail = c
            else:
                head = c + 1
        
        return -1
    

n = 5
v = 4
s = Solution(v)
print(s.firstBadVersion(n))
