# https://leetcode.com/problems/generate-parentheses/

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def bfs(pairs, stack, rest):
            if rest <= 0:
                if stack == 0:
                    ans.append(pairs)
                return

            if stack > 0:
                bfs(pairs + ")", stack - 1, rest - 1)

            if rest > 0:
                bfs(pairs + "(", stack + 1, rest - 1)

        bfs("(", 1, n*2-1)
        return ans

sl = Solution()
print(sl.generateParenthesis(3))
