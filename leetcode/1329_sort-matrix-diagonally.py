# https://leetcode.com/problems/sort-the-matrix-diagonally/

from pprint import pprint
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if n == 1 or m == 1:
            return mat

        ans = [[0] * n for _ in range(m)]
        pprint(ans)
        c = 0
        for i in range(m):
            arr = []
            print("*")
            for j in range(i+1):
                print("**", -1-i+j, j)
                if j < n:
                    arr.append(mat[-1-i+j][j])
            arr.sort()
            for j in range(i+1):
                if j < n:
                    ans[-1-i+j][j] = arr[j]

        for i in range(n):
            arr = []
            print("-")
            for j in range(m):
                print("--", j, i+j)
                if i + j < n:
                    arr.append(mat[j][i+j])
            arr.sort()
            for j in range(m):
                if i + j < n:
                    ans[j][j+i] = arr[j]
        print(mat)
        return ans

sl = Solution()
mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
mat = [[58],[99],[1],[6],[73],[9],[60],[88],[64],[60],[39],[29],[46],[20],[78],[95],[2],[35],[20],[53],[60],[15],[94],[78],[26],[89],[87],[93],[70],[31],[94],[58],[90],[48],[60],[6],[68],[62],[32],[36],[73],[49],[45],[31],[23],[3],[73],[70],[71],[18],[14],[49],[84],[72],[59],[91],[17],[46],[93],[31],[31],[71],[52],[83],[8],[95],[49],[57],[52],[65],[83],[98],[46],[55],[44],[100],[45],[7],[59],[38],[82],[62],[25],[55],[64],[56],[89],[2],[10],[57],[26],[19],[27],[80],[12],[32],[62],[91],[68],[92]]
mat = [[3,9],[2,4],[1,2],[9,8],[7,3]]
print(sl.diagonalSort(mat))
