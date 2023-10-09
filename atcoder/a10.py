# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_j

n = int(input())
a = list(map(int, input().split()))
d = int(input())

ma = [0]
mb = [0]
for i in range(1, len(a)+1):
    if a[i-1] > ma[i-1]:
        ma.append(a[i-1])
    else:
        ma.append(ma[i-1])

    if a[-i] > mb[i-1]:
        mb.append(a[-i])
    else:
        mb.append(mb[i-1])

for _ in range(d):
    l, r = map(int, input().split())
    print(max(ma[l-1], mb[n-r]))


# TLE: 先頭を削除、先頭に追加は激遅
# ma = [0]
# mb = [0]
# maxa = 0
# maxb = 0
# for i in range(len(a)):
#     if a[i] > maxa:
#         maxa = a[i]
#     ma.append(maxa)
#     if a[-1-i] > maxb:
#         maxb = a[-1-i]
#     mb = [maxb] + mb

# for _ in range(d):
#     l, r = map(int, input().split())
#     print(max(ma[l-1], mb[r]))
