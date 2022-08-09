import bisect

n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
x = []
for i in range(q):
    t = int(input())
    i = bisect.bisect_left(a, t)
    print(n-i)

# for i in range(q):
#     print(len(list(filter(lambda t:t >= x[i], a))))
