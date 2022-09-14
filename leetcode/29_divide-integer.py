# https://leetcode.com/problems/divide-two-integers/

import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        r = dividend / divisor
        print(r)
        if r > 2**31 - 1:
            r = 2**31 - 1
        return math.floor(r) if r > 0 else math.ceil(r)
