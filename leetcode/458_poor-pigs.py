# https://leetcode.com/problems/poor-pigs/


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        trial = int(minutesToTest / minutesToDie)
        if trial >= buckets - 1:
            return 1

        for pigs in range(2, 100):
            capability = 2 ** pigs
            for n in range(1, trial + 1):
                if capability >= buckets:
                    return pigs
                print("p:{}, n:{}, capa:{}".format(pigs, n, capability))
                capability = capability * (pigs) + capability
                if capability >= buckets:
                    return pigs
        return -1


    def poorPigs2(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs

sl = Solution()
b = 1000
d = 15
t = 60
print(sl.poorPigs(b, d, t))
