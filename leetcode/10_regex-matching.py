# https://leetcode.com/problems/regular-expression-matching/
        
class Solution:

    # DP 
    def isMatch(self, s, p):
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        dp[i + 1][j + 1] |= dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]

    # WA...
    def isMatch2(self, s: str, p: str) -> bool:
        ss = []
        pp = []
        for _ in s:
            ss.append(_)
        for _ in p:
            pp.append(_)
        
        sl = len(s)
        pl = len(p)
        i = j = 0
        while i < sl and j < pl:
            print(i,j, ss[i], pp[j])
            matcher = pp[j]
            if matcher == '.' or matcher == ss[i]:
                i += 1
                j += 1
            elif matcher == '*':
                while j < pl - 1:
                    if pp[j-1] == pp[j+1]:
                        j += 1
                        pp[j-1] = pp[j]
                        pp[j] = '*'
                    else:
                        break

                if pp[j-1] == '.' or pp[j-1] == ss[i]:
                    i += 1
                else:
                    j += 1
            else:
                j += 1
        if i < sl:
            return False
        else:
            if j == pl or (j == pl - 1 and (matcher == '.' or matcher == '*')):
                return True
            else:
                return False
                
                    
sl = Solution()
s = "aaa"
p = "ab*a*c*a"
# s = "aaa"
# p = "a*a"
print(sl.isMatch(s, p))
