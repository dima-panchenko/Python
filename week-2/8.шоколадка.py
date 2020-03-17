N = int(input())
M = int(input())
K = int(input())
if N == K or M == K:
    print("YES")
elif K > N and K % N == 0 and (K < N * M):
    print("YES")
elif K > M and K % M == 0 and (K < N * M):
    print("YES")
else:
    print("NO")
