# https://leetcode.com/problems/sort-the-matrix-diagonally/

from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        ans = [[0] * n for _ in range(m)]
        print(ans)

        return ans

sl = Solution()
mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(sl.diagonalSort(mat))
