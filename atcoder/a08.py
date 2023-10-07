# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h

h, w = map(int, input().split())

x = [[0] * (w + 1)]
for i in range(1, h + 1):
    l = list(map(int, input().split()))
    xi = 0
    xl = [0]
    for j in range(1, w + 1):
        xi += l[j-1]
        xl.append(xi + x[i-1][j])
    x.append(xl)

q = int(input())
for _ in range(q):
    a,b,c,d = map(int, input().split())
    print(x[c][d] - x[c][b-1] - x[a-1][d] + x[a-1][b-1])


