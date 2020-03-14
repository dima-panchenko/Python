H = int(input())
A = int(input())
B = int(input())
day = H - A
D = A - B
day1 = ((day + D - 1) // D) + 1
print(day1)
