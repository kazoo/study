# https://leetcode.com/problems/find-and-replace-pattern/

from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def getCode(word: str) -> str:
            chars = [word[0]]
            code = [1]
            for i in range(1, len(word)):
                if word[i] in chars:
                    idx = chars.index(word[i])
                    code.append(idx)
                else:
                    code.append(len(chars) + 1)
                    chars.append(word[i])
            return code

        ans = []
        pc = getCode(pattern)
        for word in words:
            if getCode(word) == pc:
                ans.append(word)
        return ans

sl = Solution()
words = ["abc","cba","xyx","yxx","yyx"]
pattern = "abc"
print(sl.findAndReplacePattern(words, pattern))
