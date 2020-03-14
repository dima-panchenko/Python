A = int(input())
B = int(input())
N = int(input())
cost = (A * 100 + B)
cost1 = cost * N
print(cost1 // 100, cost1 % 100)
