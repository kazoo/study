# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

from collections import defaultdict
from typing import List


class Solution:
    #
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        d = defaultdict(list)
        for atk, dfn in properties:
            d[atk].append(dfn)

        weak, max_dfn = 0, -1
        for k in sorted(d.keys(), reverse=True):
            for dfn in d[k]:
                if dfn < max_dfn:
                    weak += 1

            max_dfn = max(max_dfn, max(d[k]))

        return weak

    # TLE
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        max_weak = 0
        weakers = []
        l = len(properties)
        for i in range(l):
            for j in range(l):
                if i != j :
                    if properties[i][0] < properties[j][0] and properties[i][1] < properties[j][1]:
                        weakers.append(i)
                        break
        return len(weakers)


sl = Solution()
print(sl.numberOfWeakCharacters(props))