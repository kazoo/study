# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        z = [-1] * numRows
        for i in range(numRows):
            z[i] = [-1] * (l + 1)
        # z = [['*'] * int(l/2)] * numRows
        # と、宣言すると各行が同オブジェクトの参照になってしまうらしい
        # http://goldenstate.cocolog-nifty.com/blog/2020/07/post-d3d089.html

        ans = ""
        downward = True
        i = j = 0
        for _ in s:
            z[i][j] = _
#            print("{},{} -> {}".format(i,j,z[i][j]))
            if numRows == 1:
                j += 1
                continue
            if (i > 0 or j > 0) and i == 0 or i == numRows - 1:
                downward = not downward
            if downward:
                i += 1
            else:
                i -= 1
                j += 1

        for i in range(numRows):
            for j in range(l):
                if type(z[i][j]) is str:
                    ans += z[i][j]
        
        return ans


s = Solution()
# w = "PAYPALISHIRING"
w = "A"
rows = 1
print(s.convert(w, rows))
