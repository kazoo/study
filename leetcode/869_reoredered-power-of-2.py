# https://leetcode.com/problems/reordered-power-of-2/

from collections import defaultdict
from typing import Collection, Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # 文字数ごとに2^nを格納
        powers = defaultdict()
        i = 0
        while(True):
            p = 2 ** i
            l = len(str(p))
            if p <= 10 ** 9:
                if l in powers:
                    powers[l].append(str(p))
                else:
                    powers[l] = [str(p)]
            else:
                break
            i += 1

        for v in powers[len(str(n))]:
            # v を並べ替えて n が作れるか
            if Counter(v) == Counter(str(n)):
                return True
        return False

    # TLE
    def reorderedPowerOf2_2(self, n: int) -> bool:
        powers = []
        i = 0
        while(True):
            if 2 ** i <= 10 ** 9:
                powers.append(str(2 ** i))
            else:
                break
            i += 1

        print(powers)
        def permutate(numstr):
            if len(numstr) == 1:
                return [numstr]

            result = []
            for i in range(len(numstr)):
                rest = permutate(numstr[:i] + numstr[i+1:])
                for _ in rest:
                    result.append(numstr[i] + _)
            return result

        permute = permutate(str(n))
        # print(permute)
        return len(set(powers) & set(permute)) > 0

sl = Solution()
n = 254432353
print(sl.reorderedPowerOf2(n))
