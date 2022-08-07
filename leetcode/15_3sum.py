# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def combinations(nums, r):
            if r == 1:
                return [[v] for v in nums]
            result = set()
            for n, val in enumerate(nums):
                rest = combinations(nums[n+1:], r-1)

                for _ in rest:
                    comb = sorted([val] + _)
#                    if comb not in result:
                    result.add(tuple(comb))
                    # if comb not in result and sum(comb) == 0 and len(comb) == 3:
                    #     print("{}, sum:{}".format(comb, sum(comb)))
#                    if sum(comb) == 0: print(comb, sum(comb))
                    # if sorted([val] + _) not in result:
                    #     result.append(sorted([val] + _))

                    # comb = [val] + _
                    # print(comb, sum(comb))
                    # if sum(comb) == 0 and sorted(comb) not in result:
                    #     result.append(sorted(comb))
            return result

#        return list(combinations(nums, 3))
#        return list(filter(lambda x:sum(x) == 0, combinations(nums, 3)))
        return list(map(lambda x:list(x), filter(lambda x:sum(x) == 0, list(combinations(nums, 3)))))



sl = Solution()
# nums = [-1,0,1,2,-1,4]
nums = [0,7,-4,-7,0,14,-6,-4,-12,11,4,9,7,4,-10,8,10,5,4,14,6,0,-9,5,6,6,-11,1,-8,-1,2,-1,13,5,-1,-2,4,9,9,-1,-3,-1,-7,11,10,-2,-4,5,10,-15,-4,-6,-8,2,14,13,-7,11,-9,-8,-13,0,-1,-15,-10,13,-2,1,-1,-15,7,3,-9,7,-1,-14,-10,2,6,8,-6,-12,-13,1,-3,8,-9,-2,4,-2,-3,6,5,11,6,11,10,12,-11,-14]
print(sl.threeSum(nums))
