# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        ans = ""
        for i in range(l):
            if len(ans) > l - i:
                break

            ss = ""
            for j in range(i,l):
                if s[j] in ss:
                    break
                ss += s[j]
            if len(ss) > len(ans):
                ans = ss
        return len(ans)

s = Solution()
print(s.lengthOfLongestSubstring(" "))
