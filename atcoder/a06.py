# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ai

n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [0]
for i in range(len(a)):
    b.append(b[i] + a[i])

for _ in range(q):
    l, r = map(int, input().split())
    print(b[r] - b[l-1])



         
