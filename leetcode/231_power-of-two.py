# https://leetcode.com/problems/power-of-two/



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        powers = []
        for i in range(31):
            powers.append(2**i)
            
        for _ in powers:
            if _ == n:
                return True
        return False

    # 1.n = 100000, then n - 1 = 011111 and n & (n-1) = 000000, so if it is power of two, result is zero
    # 2.n = 101110, then n - 1 = 101101 and n & (n-1) = 101100, number is not power of two and result is not zero.
    def isPowerOfTwo2(self, n: int) -> bool:
        return n > 0 and not (n & n-1)
