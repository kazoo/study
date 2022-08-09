n,m = map(int, input().split())
s = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    s[a].append(b)
    s[b].append(a)

    if len(s[a]) > 2 or len(s[b]) > 2:
        print("No")
        exit(0)

def dfs(current, prev=-1):
    if visited[current] == True:
        print('No')
        exit(0)

    visited[current] = True
    for to in s[current]:
        if prev == to:
            continue
        dfs(to, current)

visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)

print("Yes")
