# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        started = False
        ans = 0
        for _ in s:
            if not started:
                if _ == ' ':
                    continue
                
                started = True
                if '0' <= _ and _ <= '9':
                    ans = int(_)
                elif _ == '-':
                    negative = True
                elif _ == '+':
                    ans = 0
                else:
                    break
            else:
                if '0' <= _ and _ <= '9':
                    ans = ans * 10 + int(_)
                else:
                    break
        
        if ans >= 2 ** 31:
            return (-2 ** 31) if negative else (2 ** 31 - 1)
        else:
            return -ans if negative else ans
            
s = Solution()
w = "words and 987"
print(s.myAtoi(w))
