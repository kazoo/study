# https://leetcode.com/problems/out-of-boundary-paths/

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        def dfs(x, y, steps, paths):
            keystr = "{0}:{1}:{2}".format(x, y, steps)
            if keystr in memo: 
                return paths + memo[keystr]

            if x < 0 or y < 0 or x >= n or y >= m:
                return paths + 1

            if steps > 0:
                memo[keystr] = dfs(x+1, y, steps-1, paths) + dfs(x, y+1, steps-1, paths) + dfs(x-1, y, steps-1, paths) + dfs(x, y-1, steps-1, paths)
                return memo[keystr]
            return paths
        
        return dfs(startColumn, startRow, maxMove, 0) % 1000000007

s = Solution()
m = 8
n = 7
maxMove = 16
startRow = 1
startColumn = 5
print(s.findPaths(m, n, maxMove, startRow, startColumn)) # 102984580

