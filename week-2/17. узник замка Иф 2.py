A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if D >= A or D >= B or D >= C:
    if E >= A or E >= B or D >= C:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
