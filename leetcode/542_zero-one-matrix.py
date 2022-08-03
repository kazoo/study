# https://leetcode.com/problems/01-matrix/submissions/


import collections
from math import inf
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        h = len(mat)
        w = len(mat[0])
        ans = [[inf] * w for _ in range(h)]
        
        def search_zero(si, sj) -> int:
            q = collections.deque([(si, sj)])
            step = 0
            visited = [[False] * w for _ in range(h)]

            while q:
                l = len(q)
                for i in range(l):
                    i,j = q.popleft()
                    print("mat[{}][{}] -> {}, step:{}".format(i, j, mat[i][j], step))
                    visited[i][j] = True
                    if mat[i][j] == 0:
                        return step
                
                    for x,y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                        if 0 <= x < h and 0 <= y < w and not visited[x][y]:
                            q.append((x,y))
                step += 1
            return step
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                elif ans[i][j] == inf:
                    ans[i][j] = search_zero(i, j)
        
        return ans

input = [[0,0,0],[0,1,0],[1,1,1]]
sl = Solution()
print(sl.updateMatrix(input))
