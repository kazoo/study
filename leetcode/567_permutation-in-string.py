# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        
        ss1 = sorted(s1)
        for i in range(l2):
            if i <= l2 - l1:
                if s2[i] in s1 and ss1 == sorted(s2[i:i+l1]):
                    return True
            else:
                break
        return False

sl = Solution()
a = "ab"
b = "aahogebahoge"

print(sl.checkInclusion(a, b))
