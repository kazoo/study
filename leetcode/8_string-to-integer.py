# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        started = False
        ans = 0
        for _ in s:
            if not started:
                if _ == ' ' or _ == '+':
                    continue
                if _ == '-':
                    negative = True
                elif '0' <= _ and _ <= '9':
                    ans = int(_)
                    started = True
                else:
                    break
            else:
                if _ == ' ':
                    break
                ans = ans * 10 + int(_)
        
        return -ans if negative else ans
            
s = Solution()
w = "words and 987"
print(s.myAtoi(w))
