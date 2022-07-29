# https://leetcode.com/problems/valid-parentheses/

class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
        
    def isValid2(self, s: str) -> bool:
        stack = [[s[0], 1]]
        
        def isPaired(p: str):
            return len(stack) > 0 and ((p == '}' and stack[-1][0] == '{') or (p == ')' and stack[-1][0] == '(') or (p == ']' and stack[-1][0] == '['))
        
        def isFirst(p: str):
            return p == '{' or p == '(' or p == '['
            
            
        for i in range(1, len(s)):
            if isFirst(s[i]):
                if len(stack) > 0 and s[i] == stack[-1][0]:
                    stack[-1][1] += 1
                else:
                    stack.append([s[i], 1])
            else:
                if isPaired(s[i]):
                    if stack[-1][1] == 1:
                        del stack[-1]
                    else:
                        stack[-1][1] -= 1
                    
                else:
                    return False
            
        return len(stack) == 0
            
sl = Solution()
s = "[])"
print(sl.isValid(s))
