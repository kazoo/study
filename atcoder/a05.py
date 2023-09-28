# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_e
n,m = map(int, input().split())

if 3 * n < m:
    print(0)
    exit()

ans = 0
for i in range(1, n+1):
    if i > m - 2:
        break
    for j in range(1, n+1):
        if i + j > m - 1:
            break
        if m - (i + j) <= n:
            ans += 1
        # for k in range(1, n+1):
        #     print(i, j, k)
        #     if i + j + k > m:
        #         break
        #     if i + j + k == m:
        #         print(i, j, k)
        #         ans += 1
print(ans)
