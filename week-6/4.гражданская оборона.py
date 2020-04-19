colVillage = int(input())
listDisVil = list(map(int, input().split()))
colBunker = int(input())
listDisBun = list(map(int, input().split()))
for i in range(colVillage):
    listDisVil[i] = (listDisVil[i], i)
for i in range(colBunker):
    listDisBun[i] = (listDisBun[i], i)


def distance(a):
    return a[0]


listDisVil.sort(key=distance)
listDisBun.sort(key=distance)
print(*listDisVil)
print(*listDisBun)
