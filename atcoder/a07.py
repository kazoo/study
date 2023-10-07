# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g

d = int(input())
n = int(input())
a = [0] * d

for _ in range(n):
    l,r = map(int, input().split())
    a[l-1] += 1
    if r < d:
        a[r] -= 1

s = 0
for ai in a:
    s += ai
    print(s)


