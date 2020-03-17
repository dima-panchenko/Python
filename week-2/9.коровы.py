N = int(input())
if N % 10 == 1 and N != 11:
    print(N, "korova")
elif 1 < N % 10 < 5:
    if N == 12 or N == 13 or N == 14:
        print(N, "korov")
    else:
        print(N, "korovy")
else:
    print(N, "korov")
