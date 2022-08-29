# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from collections import deque
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        l = len(digits)
        if l == 0:
            return []
        q = deque([('', l)])
        ans = []
        while q:
            (c, rest) = q.popleft()
            if rest == 0:
                ans.append(c)
                continue
            d = digits[l-rest]
            for _ in chars[d]:
                q.append((c + _, rest - 1))
        return ans






sl = Solution()
d = "23"
print(sl.letterCombinations(d))
