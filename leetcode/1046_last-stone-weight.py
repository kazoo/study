# https://leetcode.com/problems/last-stone-weight/submissions/

from bisect import insort_left
from typing import List

class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while stones:
            s1 = stones.pop()  # the heaviest stone
            if not stones:  # s1 is the remaining stone
                return s1
            s2 = stones.pop()  # the second-heaviest stone; s2 <= s1
            if s1 > s2:
                # the remaining stone will be s1-s2
                # binary-insert the remaining stone into stones
                insort_left(stones, s1-s2)
            # else s1 == s2; both stones are destroyed
        return 0  # if no more stones remain

    # too slow...
    def lastStoneWeight2(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]

        stones.sort()
        diff = stones[-1] - stones[-2]
        while len(stones) > 1:
            a = stones.pop(-1)
            b = stones.pop(-1)
            if a - b > 0:
                stones.append(a - b)
                stones.sort()


        return stones[0] if len(stones) > 0 else 0
