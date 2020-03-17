n = int(input())
i = 1
bol = 1
while i <= n:
    if i == n:
        bol = 1
    else:
        bol = 0
    i *= 2
if bol == 1:
    print("YES")
else:
    print("NO")
