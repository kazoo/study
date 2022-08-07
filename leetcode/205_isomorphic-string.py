# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l = len(s)
        if len(t) != l:
            return False
        
        pattern_s = []
        pattern_t = []
        appeared_s = []
        appeared_t = []
        for i in range(l):
            if s[i] in appeared_s:
                pattern_s.append(appeared_s.index(s[i]))
            else:
                appeared_s.append(s[i])
                pattern_s.append(appeared_s.index(s[i]))
                
            if t[i] in appeared_t:
                pattern_t.append(appeared_t.index(t[i]))
            else:
                appeared_t.append(t[i])
                pattern_t.append(appeared_t.index(t[i]))
            
            print(pattern_s, pattern_t)
            if pattern_s != pattern_t:
                return False
        return True
                

sl = Solution()
s = "title"                
t = "paper"
print(sl.isIsomorphic(s, t))
