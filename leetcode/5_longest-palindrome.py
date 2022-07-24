# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        ans = s[0]
        for i in range(1, l*2):
            ss = ""
            head = int(i/2)
            tail = int(i/2 + 0.5)
            while head >= 0 and tail < l:
                if s[head] == s[tail]:
                    ss = s[head:tail+1]
                    head -= 1
                    tail += 1
                    if len(ss) > len(ans):
                        ans = ss
                else:
                    break

        return ans

    # TLE
    def longestPalindrome3(self, s: str) -> str:
        l = len(s)
        ans = s[0]
        for i in range(l):
            if len(ans) > l - i:
                break

            ss = ""
            for j in range(l-i):
                print("l: {0}, i: {1}, j:{2}".format(l, i, j))
                print("substring", s[i:l-j])
                print(len(ans), l-i-j)
                if len(ans) > l - i - j:
                    break

                kaibun = True
                ss = s[i:l-j]
                    
                for k in range(int(len(ss)/2)):
                    print("k: {0}, -k: {1}".format(ss[k], ss[-1-k]))
                    if ss[k] != ss[-1-k]:
                        kaibun = False
                        break
                
                if kaibun and len(ss) > len(ans):
                    print("ans:{} ".format(ans))
                    ans = ss
                    break

        return ans
                    
s = Solution()
# w = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

w = "aaabcaaa"
ans = s.longestPalindrome(w)
print("ans", ans)
print("input/output len:", len(w), len(ans))
