# https://leetcode.com/problems/subarray-sum-equals-k/
import collections
from pprint import pprint
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        c = collections.defaultdict(int)
        c[0] = 1
        ans = 0
        sum = 0
        for i in range(l):
            sum += nums[i]
            ans += c[sum - k]
            c[sum] += 1
        
        return ans
    
# 累積和：先頭からとある点までの合計
# 例
# sum[i]: 0からiまでの累積和
# sum[i] = 10
# k = 3の時
# sum[j] = 7のものがあれば i-jの範囲が答え

            
    # TLE
    def subarraySum2(self, nums: List[int], k: int) -> int:
        l = len(nums)
        for i in range(l-1):
            nums[i + 1] += nums[i]
            
        c = {}
        res = 0
        c = collections.defaultdict(int)
        for i in range(l):
            cur = 0
            for j in range(i, l):
                cur = nums[j] - (nums[i-1] if i > 0 else 0)
#                print("{}:{}, nums[j]:{}, nums[i]:{} cur:{}".format(i, j, nums[j], (nums[i-1] if i > 0 else 0), cur))
                c[cur] += 1
        return c[k]

s = Solution()
nums = [1,2,3, 3]
k = 3
print(s.subarraySum(nums, k))
