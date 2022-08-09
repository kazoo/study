# 

import collections

n = int(input())
a = list(map(int, input().split()))

ans = 0
l = len(a)
c = collections.defaultdict(int)
c[0] = 1
sum = 0
for i in range(l):
    sum += a[i]
    ans += c[sum]
    c[sum] += 1

print(ans)

# TLE...
# sums = [0]
# for i in range(1, l+1):
#     sums.append(sums[i-1] + a[i-1])
#
# for i in range(0, l):
#     for j in range(i, l):
#         if sums[j+1] - sums[i] == 0:
#             ans += 1

# print(ans)
