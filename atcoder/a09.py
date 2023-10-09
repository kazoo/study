# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_i

import pprint


h, w, n = map(int, input().split())

a = [[0] * (w+1) for _ in range(h+1)]

for _ in range(n):
    i1,j1,i2,j2 = map(int, input().split())
    i1 -= 1
    j1 -= 1

    a[i1][j1] += 1
    a[i1][j2] -= 1
    a[i2][j1] -= 1
    a[i2][j2] += 1

for i in range(h):
    for j in range(w):
        if j - 1 >= 0:
            a[i][j] += a[i][j-1]

for i in range(h):
    for j in range(w):
        if i - 1 >= 0:
            a[i][j] += a[i-1][j]

# pprint.pprint(a)

for i in range(h):
    print(*a[i][:-1])
