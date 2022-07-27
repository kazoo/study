# 

from typing import List

class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        l = len(nums)
        while i < l:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                l -= 1
            else:
                i += 1
        print(nums)

    # not in-place
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ans = []
        # zeros = 0
        # for _ in nums:
        #     if _ == 0:
        #         ans.append(0)
        #         zeros += 1
        #     else:
        #         ans.insert(len(ans)-zeros, _)
        # return ans

    # TLE
    def moveZeroes3(self, nums: List[int]) -> None:
        l = len(nums)
        zeros = 0
        nonzeros = 0
        while zeros + nonzeros < l:
            if nums[nonzeros] != 0:
                nonzeros += 1
                continue
            else:
                for i in range(nonzeros, l-1):
                    nums[i] = nums[i+1]
                nums[-1-zeros] = 0
                zeros += 1

        print(nums)
s = Solution()
# nums = [0,0,1]
nums = [0,1,0,3,12]
print(s.moveZeroes(nums))
