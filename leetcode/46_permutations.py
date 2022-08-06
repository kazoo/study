# https://leetcode.com/problems/permutations/

from typing import List
import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perm(mylist):
            # 最後の1文字ならリストにしてそのまま返す
            if len(mylist) == 1:
                return [mylist]
            result = []
            for i, val in enumerate(mylist):
                # 1文字抜いて残りを再起呼び出し
                rest = perm(mylist[:i] + mylist[i+1:])
                for _ in rest:
                    # 抜いた1文字と再合成
                    result.append([val] + _)
            return result
        return perm(nums)

    def power(self, n) -> int:   
        if n <= 1:
            return n
        return n * self.power(n-1)


sl = Solution()
print(sl.permute([1,2,3]))
