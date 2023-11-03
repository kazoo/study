n,k = map(int, input().split())

def g(x, asc) -> int:
    a = []
    r = 0
    while x > 0:
        a.append(x % 10)
        x //= 10

    l = len(a) - 1
    a.sort(reverse=asc)
    for ai in a:
        r += 10 ** l * ai
        l -= 1
    return r 

for _ in range(k):
    n = g(n, True) - g(n, False)

print(n)

