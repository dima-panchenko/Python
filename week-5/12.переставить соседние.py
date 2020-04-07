a = list(map(int, input().split()))
b = []

if len(a) % 2 == 0:
    a1 = a[::2]
    a2 = a[1::2]
else:
    a1 = a[::2]
    a2 = a[1:len(a) - 1:2]

for i in range(len(a2)):
        b.append(a2[i])
        b.append(a1[i])

if len(a) % 2 != 0:
    b.append(a[-1])

print(' '.join(map(str, b)))
