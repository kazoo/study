# https://leetcode.com/problems/01-matrix/submissions/


import collections
from math import inf
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(matrix), len(matrix[0])
        queue = collections.deque()
        res = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # The distance to itself is 0 and add all sources here to queue
                    res[i][j] = 0
                    queue.append((i, j))

        while queue:
            curI, curJ = queue.popleft()
            for i, j in dirs:
                neighBorI, neighBorJ = curI + i, curJ + j
                # Validate all the neighbors and validate the distance as well
                if 0 <= neighBorI < m and 0 <= neighBorJ < n and res[neighBorI][neighBorJ] == -1:
                    res[neighBorI][neighBorJ] = res[curI][curJ] + 1
                    queue.append((neighBorI, neighBorJ))

        return res


    # TLE
    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
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
