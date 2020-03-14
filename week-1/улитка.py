H = int(input())
A = int(input())
B = int(input())
day = 0
for i in range(H):
    day += 1
    H = H - A
    if H <= 0:
        print(day)
        break
    else:
        H = H + B
