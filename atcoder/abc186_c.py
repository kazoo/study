# https://atcoder.jp/contests/abc186/tasks/abc186_c

n = int(input())
def isInclude(x, target, base):
    while x > 0:
        if x % base == target:
            return True
        x //= base
    return False

r = 0
for i in range(1, n+1):
    if not (isInclude(i, 7, 8) or isInclude(i, 7, 10)):
        r += 1
print(r)

