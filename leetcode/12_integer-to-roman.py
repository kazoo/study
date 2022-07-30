# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        # I, II, III, IV, V, VI, VII, VIII, IX
        # X, XX, XXX, XL, L, LX, LXX, LXXX, XC
        # C, CC, CCC, CD, D, DC, DCC, DCCC, CM
        # M, MM, MMM
        table = [["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["M", "MM", "MMM"]]
        
        ans = ""
        l = len(str(num))
        i = 0
        while num > 0:
            digit = int(num % 10)
            if digit > 0:
                ans = table[i][digit - 1] + ans
            i += 1
            num /= 10
        return ans
        

sl = Solution()
n = 1234
print(sl.intToRoman(n))