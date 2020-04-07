n = int(input())
intList = list(map(int, input().split()))
x = int(input())
a = 1000
i = -1
List = [0]
while i < len(intList) - 1:
    i += 1
    if intList[i] > 0:
        k = abs(x - intList[i])
    else:
        k = abs(intList[i]) - (x)
    if k <= a:
        a = k
        List.pop()
        List.append(intList[i])
print(*List)
