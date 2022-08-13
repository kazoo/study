# https://leetcode.com/problems/3sum-closest/

from math import inf
from typing import List

class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        ans = inf
        for i in range(l - 2):
            j = i + 1
            k = l - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if target - sum == 0:
                    return sum

                if abs(target - sum) < abs(target - ans):
                    ans = sum

                if sum >= target:
                    k -= 1
                if sum < target:
                    j += 1
        return ans


    # TLE
    def threeSumClosest2(self, nums: List[int], target: int) -> int:
        ans = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    c = nums[i] + nums[j] + nums[k]
                    print(ans, c, abs(target - c), abs(target - ans))
                    if abs(target - c) < abs(target - ans):
                        print("------- {}, {}, {}, {}".format(ans, c, abs(target - c), abs(target - ans)))
                        ans = c
        return ans

sl = Solution()
nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2
nums = [-1,2,1,-4]
target = 1
nums = [-233,-721,225,-747,-656,-454,-85,-292,164,-160,-763,-970,-807,627,-114,-45,-931,37,393,-812,196,404,942,509,-200,216,316,927,125,114,219,-505,281,211,-749,-14,832,-237,208,533,949,-264,775,428,-106,425,-502,-523,997,-998,-636,-743,-361,-1,-164,-507,624,380,-785,-286,203,687,968,-679,-395,-981,854,62,-101,88,-541,-802,-405,-266,541,-550,-445,131,92,483,-875,-222,-238,867,787,-308,852,-962,-86,-408,571,-799,-359,190,386,-908,-48,994,-571,427,512,396,11,480,572,-28,444,145,-797,-649,-688,-664,-810,-311,185,171,332,794,635,-78,232,-727,43,172,-867,556,253,335,84,717,-734,-767,-967,-135,289,697,612,952,201,818,-321,844,970,-117,679,-755,542,-697,104,992,803,-882,955,-129,737,-71,946,401,665,-120,295,240,16,-176,959,377,-332,-599,-702,951,-831,-706,506,263,-126,-442,-592,-606,-821,93,911,-168,349,455,121,20,889,334,-751,676,-861,-796,-314,-364,821,515,-614,947,865,76,303,-196,275,390,812,-623,-10,236,975,-152,-110,265,488,989,322,732,-254,-217,-136,-470,-888,659,179,-453,-183]
target = 7359
print(sl.threeSumClosest(nums, target))
