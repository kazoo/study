# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from functools import reduce
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(reduce(lambda a,b: a+b, matrix))[k-1]

    # binary search
    def kthSmallest2(self, matrix, k):
        n, start, end = len(matrix), matrix[0][0], matrix[-1][-1]
        
        def check(m):
            i, j, cnt = 0, n-1, 0
            for i in range(n):
                while j >= 0 and matrix[i][j] > m: j -= 1
                cnt += (j + 1)
            return cnt
         
        while start < end:
            mid = (start + end)//2
            if check(mid) < k:
                start = mid + 1
            else:
                end = mid
                
        return start
sl = Solution()
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(sl.kthSmallest(matrix, k))

