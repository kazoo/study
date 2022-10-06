# https://leetcode.com/problems/sqrtx/

class Solution:
    # O(√x)
    def mySqrt(self, x: int) -> int:
        for i in range(0, x+1):
            if i * i == x:
                return i
            if i * i > x:
                return i - 1

    def mySqrt2(self, x: int) -> int:
        # For x = 0 and x = 1
        if x <= 1: return x

        start = 2
        end = x

        # Apply Binary Search since range 1 to x is in sorted order
        while start <= end:
            mid = start + (end - start)  // 2

            square = mid * mid
            # If square of a number is equal to x, we got the square root
            if square == x: return mid
            # If square of a number if less than x, go for a bigger number
            if square < x: start = mid + 1
            # If square of a number if more than x, go for a smaller number
            else: end = mid - 1

        # If the number is not a perfect square, return the value "end"
        return end

x = 4
s = Solution()
print(s.mySqrt(x))
