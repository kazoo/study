
from collections import deque
import itertools
from pprint import pprint
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
                    # 上で抜いた要素から始まる順列を生成する
                    result.append([val] + _)
            return result
        return permutate(nums)

    # n個の要素からr個取り出したい場合
    def getPermutations(self, nums: List, r = None) -> List:
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

    # ライブラリで 1-liner
    def getPermutations2(self, nums: List, r = None) -> List:
        return itertools.permutations(nums, r)

    # 重複なしコンビネーション
    def getCombinations(self, nums: List, r = None) -> List:
        if r == None:  # rが設定されていないときはnumsの要素数に初期化
            r = len(nums)

        def combinations(my_list, r):
            if r == 1:
                return [[val] for val in my_list]  # my_listを要素数1の組合せの組にする
            else:
                result = []
                for i, val in enumerate(my_list):
                    rest = combinations(my_list[i+1:], r-1)  # (i+1)番目以降の要素を使えばいい
                    for rest_perm in rest:
                        perm = [val] + rest_perm
                        result.append(perm)
                return result
        return combinations(nums, r)

    # n種類からr個（n<r）を使った順列（DFS）
    def getPermutations3(self, nums: List, r: int) -> List:
        q = deque()

        # 適切に枝刈りしないとすぐTLEするので問題に応じてDPの方が良さそう
        def dfs(n, level):
            if level == 1:
                q.append(n)
                return n

            for _ in nums:
#                if sum(n) + _ <= target:  # 枝刈りの例
                dfs(n + [_], level - 1)

        for i in range(1, r + 1):
            for _ in nums:
#                if _ <= target:  # 枝刈り
                dfs([_], i)
        return q

p = Permutation()
n = [_ for _ in range(4)]
r  = 3
print(p.getPermutations(n))
print(p.getPermutations(n, r))
print(p.getCombinations(n, r))
print(p.getPermutations3(n, r))

# e = p.getPermutations2(n, r)
# for _ in e:
#     print(_)
