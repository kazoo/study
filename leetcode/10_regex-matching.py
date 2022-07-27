# https://leetcode.com/problems/regular-expression-matching/
        
class Solution:


    def match(self, s, i, p, j):
        if i == len(s) or j == len(p):
            return False
        
        return p[j] == '.' or s[i] == p[j]
    
    def helper(self, s, i, p, j):
        # Base Cases
        if j == len(p):
            return i == len(s)
        # to cover the case of "abc" ".*"
        if i > len(s):
            return False
        
        # 1. if second is * p[i+1]
        if j < len(p)-1 and p[j+1] == '*':
            # Zero means advance p[j+2]
            # one or more compare and advance if match
            return (self.match(s, i, p, j) and self.helper(s, i+1, p, j)) or self.helper(s, i, p, j+2)
        
        # 2. Match either same or '.'
        if self.match(s, i, p, j):
            return self.helper(s, i+1, p, j+1)
        
        # 3. No match or *
        return False
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.helper(s, 0, p, 0)

    # DP 
    def isMatch3(self, s, p):
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
p = "a*a*aaaa"
# s = "aaa"
# p = "a*a"
print(sl.isMatch(s, p))
