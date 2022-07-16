# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        merged = sorted(nums1)
        l = len(merged)
        if l % 2 == 1:
            return merged[int(l/2)]
        else:
            return (merged[int(l/2) - 1] + merged[int(l/2)])/2

l1 = [1,3]
l2 = [2,4]
s = Solution()
print(s.findMedianSortedArrays(l1, l2))
