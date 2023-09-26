s = input()
l = len(s)
ans = s[0]
for i in range(1, l*2):
    ss = ""
    head = int(i/2)
    tail = int(i/2 + 0.5)
    while head >= 0 and tail < l:
        if s[head] == s[tail]:
            ss = s[head:tail+1]
            head -= 1
            tail += 1
            if len(ss) > len(ans):
                ans = ss
        else:
            break

print(len(ans))
