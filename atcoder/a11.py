# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_k

n, x = map(int, input().split())
a = list(map(int, input().split()))

l = 0
r = n
while l < r:
    m = int((l + r) / 2)
    if a[m] == x:
        print(m+1)
        exit(0)
    if a[m] > x:
        r = m
    else:
        l = m

