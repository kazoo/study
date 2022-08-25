# https://leetcode.com/problems/count-vowels-permutation/

class Solution:


    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (10**9 + 7)

    # TLE
    def countVowelPermutation2(self, n: int) -> int:
        if n == 1:
            return 5

        self.ans = 0
        self.memo = {1: 5}
        def permutate(vowels, rest):
            if rest == 0:
                self.ans += 1
                print(vowels)
                return

            if vowels[-1] == 'a':
                permutate(vowels + 'e', rest - 1)
            if vowels[-1] == 'e':
                permutate(vowels + 'a', rest - 1)
                permutate(vowels + 'i', rest - 1)
            if vowels[-1] == 'i':
                permutate(vowels + 'a', rest - 1)
                permutate(vowels + 'e', rest - 1)
                permutate(vowels + 'u', rest - 1)
                permutate(vowels + 'o', rest - 1)
            if vowels[-1] == 'o':
                permutate(vowels + 'i', rest - 1)
                permutate(vowels + 'u', rest - 1)
            if vowels[-1] == 'u':
                permutate(vowels + 'a', rest - 1)

        permutate('a', n-1)
        permutate('e', n-1)
        permutate('i', n-1)
        permutate('o', n-1)
        permutate('u', n-1)
        return self.ans

sl = Solution()
n = 144
print(sl.countVowelPermutation(n))
