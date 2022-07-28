# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:

    # tuned!
    def reverseWords(self, s: str) -> str:
        ans = ""
        l = r = 0
        while r < len(s):
            if s[r] != ' ':
                r += 1
                if r == len(s):
                    ans += " " + s[l:r][::-1]
            else:
                ans += s[l:r][::-1] # [start:end:step]
                l = r
                r += 1
        return ans[1:]
                


    # 1st try
    def reverseWords3(self, s: str) -> str:
        ans = ""
        l = len(s)
        ss = 0
        for i in range(l+1):
            if i == l or s[i] == ' ':
                if ss != 0:
                     ans += " "
                ans += self.getReverseWord(s[ss:i])
                i += 1
                ss = i
        return ans
                
    def getReverseWord(self, s: str):
        ss = ""
        for i in range(len(s)):
            ss += s[-1-i]
        return ss

    # 1 liner いけるらしい
    def reverseWords2(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]

        # That's a bit shorter than the more obvious one:
        # return ' '.join(x[::-1] for x in s.split())

s = Solution()
w = "Gods Ding"
print(s.reverseWords(w))

# ss = [0, 10, 20, 30, 40, 50]
# print(ss[::-1])