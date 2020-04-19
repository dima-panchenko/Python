n = int(input())
listMan = []
for i in range(n):
    man = input().split()
    listMan.append(man)


def mySort(x):
    b = int(x[1])
    return -b


listMan.sort(key=mySort)
for a in listMan:
    print(a[0])
