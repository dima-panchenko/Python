N = int(input())
M = N // 60
H = M // 60
S = (N - ((M % 60) * 60 + (H % 23) * 3600)) % 60
M1 = (M % 60) // 10
M2 = (M % 60) % 10
S1 = S // 10
S2 = S % 10
print(H % 24, end=":")
print(M1, M2, sep="", end=":")
print(S1, S2, sep="")
