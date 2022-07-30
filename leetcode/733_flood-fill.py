# https://leetcode.com/problems/flood-fill/

import collections
from pprint import pprint
from typing import List

class Solution:
    # DFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i, j):
            image[i][j] = color
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                    dfs(x, y)
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != color: 
            dfs(sr, sc)
        return image

    # BFS
    # 組み込みのリストlistをキューやスタック、デック（両端キュー）として使うことも可能だが、
    # リストでは先頭の要素に対する削除や追加（挿入）は処理速度が遅いためdequeのほうが効率的
    # dequeには両端以外の要素へのアクセスが遅いというデメリットもあるので注意。
    def floodFill2(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != color: 
            q = collections.deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = color
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old: 
                        q.append((x, y))
        return image


    def floodFill3(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        h = len(image)
        w = len(image[0])
        
        def fill(r: int, c: int, previous: int, color: int):
            if r < 0 or c < 0 or r >= h or c >= w or image[r][c] == color or image[r][c] != previous:
                return
            
            current = image[r][c]
            image[r][c] = color
            fill(r-1, c, current, color)
            fill(r+1, c, current, color)
            fill(r, c+1, current, color)
            fill(r, c-1, current, color)
            return

        fill(sr, sc, image[sr][sc], color)
        return image


sl = Solution()
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1
# sc = 1
# color = 2
image = [[0,0,0],[1,0,0]]
sr = 1
sc = 0
color = 2
pprint(sl.floodFill(image, sr, sc, color))
