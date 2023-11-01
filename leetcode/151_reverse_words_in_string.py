# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        w = ""
        for c in s:
            if c == " ":
                if w != "":
                    words.append(w)
                w = ""
            else:
                w += c
        words.append(w)
        return (' '.join(map(str, reversed(words))).strip())


    def reverseWords2(self, s: str) -> str:
        words = []
        w = ""
        for c in s:
            if c == " ":
                words.append(w)
                w = ""
            else:
                w += c
        words.append(w)
        print(' '.join(map(str, reversed(words))))

s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords(" hello world "))
