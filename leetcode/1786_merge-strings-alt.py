# https://leetcode.com/problems/merge-strings-alternately/


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        l1 = len(word1)
        l2 = len(word2)
        for i in range(max(l1, l2)):
            if l1 > i:
                ans += (word1[i])
            if l2 > i:
                ans += (word2[i])
        return ans
        

word1 = "abcdef"
word2 = "pqr"
s = Solution()
print(s.mergeAlternately(word1, word2))


