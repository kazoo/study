# https://leetcode.com/problems/pascals-triangle/

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p = [[1]]
        for i in range(1, numRows):
            pp = [int] * (i + 1)
            pp[0] = 1
            pp[-1] = 1
            for j in range(1, i):
                pp[j] = p[i-1][j-1] + p[i-1][j]
            p.append(pp)
                
        return p

s = Solution()
print(s.generate(5))
