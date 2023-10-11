# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l

n,k = map(int, input().split())
a = list(map(int, input().split()))

bottom = 0
top = 10**10
mid = top // 2

def cnt(mid):
    c = 0
    for ai in a:
        c += mid // ai
    return c 

while top - bottom > 1:
    mid = (top + bottom) // 2
    if cnt(mid) < k:
        bottom = mid
    else:
        top = mid 

print(mid+1)

