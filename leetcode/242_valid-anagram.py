# 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        for _ in s:
            # dict.get() の第２引数はデフォルト値
            dic_s[_] = dic_s.get(_, 0) + 1

        for _ in t:
            dic_t[_] = dic_t.get(_, 0) + 1

        return dic_s == dic_t

    # 1 liner
    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # TLE
    def isAnagram3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for _ in s:
            if s.count(_) != t.count(_):
                return False
            s.split(_)
            t.split(_)
        return True

sl = Solution()
s = "anagram"
t = "nagaram"
print(sl.isAnagram(s, t))