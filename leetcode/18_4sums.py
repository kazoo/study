# https://leetcode.com/problems/4sum/

from collections import deque
from typing import List


class Solution:

    def fourSum(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results

    # ...
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        q = deque()

        def combinations(nlist, rlist, r):
            if r == 1:
                return [[val] for val in nlist]  # my_listを要素数1の組合せの組にする

            for i, val in enumerate(nums):
                rest = combinations(nlist[i+1:], r - 1)
                for rest_perm in rest:
                    perm = [val] + rest_perm
#                    if sum(nlist) == target and nlist not in q:
                    q.append(perm)
        # for _ in nums:
        #      dfs([_], 4)
        #  return q

    #     def combinations(my_list, r):
    #         if r == 1:
    #             return [[val] for val in my_list]  # my_listを要素数1の組合せの組にする
    #         else:
    #             result = []
    #             for i, val in enumerate(my_list):
    #                 rest = combinations(my_list[i+1:], r-1)  # (i+1)番目以降の要素を使えばいい
    #                 for rest_perm in rest:
    #                     perm = [val] + rest_perm
    #                     result.append(perm)
    #             return result
        return combinations(nums, 4)


sl = Solution()
nums = [1,0,-1,0,-2,2]
print(sl.fourSum(nums, 0))
