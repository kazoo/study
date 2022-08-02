# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from functools import reduce
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:        
        return sorted(reduce(lambda a,b: a+b, matrix))[k-1]

sl = Solution()
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(sl.kthSmallest(matrix, k))

