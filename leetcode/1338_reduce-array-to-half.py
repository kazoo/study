# https://leetcode.com/problems/reduce-array-size-to-the-half/

from collections import Counter
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        l = len(arr)
        c = Counter(arr)
        n = 0
        ans = 0
        for (val, i) in c.most_common():
            ans += 1
            n += i
            if n >= int(l/2):
                return ans
        return 0

sl = Solution()
arr = [3,3,5,6,7,7,7,8]
print(sl.minSetSize(arr))
