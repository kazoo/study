# https://leetcode.com/problems/rotting-oranges/

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    
        if len(q) == 0:
            for _ in grid:
                if 1 in _:
                    return -1
            return 0

        step = 0
        while q:
            print(q)
            l = len(q)
            for _ in range(l):
                x,y = q.popleft()
                for i,j in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                    if 0 <= i < m and 0 <= j < n and grid[i][j] > 0:
                        if grid[i][j] == 1:
                            q.append((i,j))
                            grid[i][j] = -1 # visit flag
                        elif grid[i][j] == 0:
                            grid[i][j] = -1
            if len(q) > 0:
                step += 1
        
        for _ in grid:
            if 1 in _:
                return -1
        return step

sl = Solution()
matrix = [[2,1,1],[1,1,0],[0,1,1]]  # 4
matrix = [[2,1,1],[0,1,1],[1,0,1]]  # -1
matrix = [[0]]                      # 0
matrix = [[1]]                      # -1
matrix = [[2,2],[1,1],[0,0],[2,0]]  # 1
print(sl.orangesRotting(matrix))