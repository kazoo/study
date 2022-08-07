
from typing import List

class Permutation:

    # 受け取ったリストの順列全パターンを返す
    def getPermutations(self, nums) -> List:

        def permutate(nums):
            # 最後の1要素ならリストにしてそのまま返す
            if len(nums) == 1:
                return [nums]

            result = []
            for i, val in enumerate(nums):
                # 1要素抜いて再帰呼び出し
                rest = permutate(nums[:i] + nums[i+1:])
                for _ in rest:
                    # 上で抜いた要素と結合
                    result.append([val] + _)
            return result
        return permutate(nums)

    # n個の要素からr個取り出したい場合
    def getCombinations(self, nums: List, r = None) -> List:
        if r == None:  # rが設定されていないときはnumsの要素数に初期化
            r = len(nums)

        def permutate(nums, r):
            if r == 1:
                return [[val] for val in nums]  # numsを要素数1の順列の組にする

            result = []
            for i, val in enumerate(nums):
                rest = permutate(nums[:i] + nums[i+1:], r-1)  # 取り出す数を1つ減らす
                for _ in rest:
                    result.append([val] + _)
            return result
        return permutate(nums, r)


p = Permutation()
n = [_ for _ in range(4)]
r  = 3
print(p.getPermutations(n))
print(p.getCombinations(n, r))
