a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
S = d * e
if a * b <= S or a * c <= S or b * c <= S:
    print("YES")
else:
    print("NO")
