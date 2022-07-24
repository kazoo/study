# https://leetcode.com/problems/number-of-matching-subsequences/

from pprint import pprint
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def encode(s):
            enc = [[s[0], 1]]
            for i in range(1, len(s)):
                if enc[-1][0] == s[i]:
                    enc[-1][1] += 1                
                else:
                    enc.append([s[i], 1])
            return enc
        
        enc = encode(s)
        ans = 0
        for word in words:
            eword = encode(word)
            print(eword)
            print(len(enc), len(eword))
            i = j = 0
            while i < len(enc) and j < len(eword):
#                pprint("i:{}, j:{}, s[{},{}] - w[{},{}]".format(i, j, enc[i][0], enc[i][1], eword[j][0], eword[j][1] ))

                if eword[j][0] == enc[i][0]:
                    if enc[i][1] >= eword[j][1]:
                        j += 1
                        if j == len(eword):
                            ans += 1
                    else:
                        eword[j][1] -= enc[i][1]
                i += 1

        return ans

    # TLE
    def numMatchingSubseq2(self, s: str, words: List[str]) -> int:
        enc = []
        for i in range(1, len(s)):
            cnt = 0
            if s[i] == s[i-1]:
                cnt += 1
                continue
            else:
                enc.append({s[-1]: i})
        
        ans = 0
        for word in words:
            i = 0
            for _ in s:
                if _ == word[i]:
                    i += 1
                    if i == len(word):
                        ans += 1
                        break

        return ans

s = "ricogwqznwxxcpueelcobbbkuvxxrvgyehsudccpsnuxpcqobtvwkuvsubiidjtccoqvuahijyefbpqhbejuisksutsowhufsygtwteiqyligsnbqglqblhpdzzeurtdohdcbjvzgjwylmmoiundjscnlhbrhookmioxqighkxfugpeekgtdofwzemelpyjsdeeppapjoliqlhbrbghqjezzaxuwyrbczodtrhsvnaxhcjiyiphbglyolnswlvtlbmkrsurrcsgdzutwgjofowhryrubnxkahocqjzwwagqidjhwbunvlchojtbvnzdzqpvrazfcxtvhkruvuturdicnucvndigovkzrqiyastqpmfmuouycodvsyjajekhvyjyrydhxkdhffyytldcdlxqbaszbuxsacqwqnhrewhagldzhryzdmmrwnxhaqfezeeabuacyswollycgiowuuudrgzmwnxaezuqlsfvchjfloczlwbefksxsbanrektvibbwxnokzkhndmdhweyeycamjeplecewpnpbshhidnzwopdjuwbecarkgapyjfgmanuavzrxricbgagblomyseyvoeurekqjyljosvbneofjzxtaizjypbcxnbfeibrfjwyjqrisuybfxpvqywqjdlyznmojdhbeomyjqptltpugzceyzenflfnhrptuugyfsghluythksqhmxlmggtcbdddeoincygycdpehteiugqbptyqbvokpwovbnplshnzafunqglnpjvwddvdlmjjyzmwwxzjckmaptilrbfpjxiarmwalhbdjiwbaknvcqovwcqiekzfskpbhgxpyomekqvzpqyirelpadooxjhsyxjkfqavbaoqqvvknqryhotjritrkvdveyapjfsfzenfpuazdrfdofhudqbfnzxnvpluwicurrtshyvevkriudayyysepzqfgqwhgobwyhxltligahroyshfndydvffd"
words = ["ccrubahioyaxuwzloyhqyluwoknxnydbedenrccljoydfxwaxy"]
# s = "abcde"
# words = ["a","bb","acd","ace"]
sl = Solution()
print(sl.numMatchingSubseq(s, words))
